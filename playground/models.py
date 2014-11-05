import threading
import re
import datetime
from django.db import models, IntegrityError
from django.utils import timezone
from django.db import transaction
from django.db.models import F
from django.utils.timezone import utc
from celery.utils.log import get_task_logger
from playground.custom import sanitize_string

logger = get_task_logger(__name__)


class Detector(models.Model):
    """
    The single detector
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    last_run_date = models.DateTimeField('last run date', default=None, blank=True, null=True)
    run_count = models.IntegerField('run count', default=0)
    created_at = models.DateTimeField('date created', default=datetime.datetime.utcnow().replace(tzinfo=utc))

    def was_runned_recently(self):
        return self.last_run_date >= timezone.now().replace(tzinfo=utc) - datetime.timedelta(hours=1)

    def __str__(self):
        return 'Detector {name}, "{description}" - last run: {last_run}'.format(
            name=self.name,
            description=self.description,
            last_run=self.last_run_date
        )

    ## DELETE_ME
    # @classmethod
    # @transaction.atomic
    # def get_by_name(cls, detector_name):
    #     """
    #     Get or create but for the poor-man-thread-safe version
    #
    #     :return:
    #     """
    #
    #     detector_name = sanitize_string(detector_name)
    #
    #     try:
    #         # https://docs.djangoproject.com/en/1.6/releases/1.6.3/#select-for-update-requires-a-transaction
    #         with transaction.atomic():
    #             # https://docs.djangoproject.com/en/1.6/ref/models/querysets/#select-for-update
    #             try:
    #                 detector_found_or_created = Detector.objects.get(name=detector_name)
    #             except Detector.DoesNotExist:
    #                 detector_found_or_created = None
    #             if not detector_found_or_created:
    #                 logger.info('Creating Detector \"%s\" from %s' % (detector_name, threading.current_thread()))
    #                 detector_found_or_created = Detector.objects.create(
    #                     name=detector_name,
    #                     description='%s Detector' % detector_name
    #                 )
    #             return detector_found_or_created
    #     except IntegrityError as not_thread_safe_as_expected:
    #         logger.error('Some trivial concurrency problem occured here, ya know... %s' % not_thread_safe_as_expected)
    #         return Detector.objects.filter(name=detector_name).first()

    ## DELETE_ME
    # def get_implementation(self):
    #     """
    #     Return the Class corresponding at the detector name
    #
    #     :return:
    #     """
    #     print("Ready to EVAL : %s for %s" % (self.name, self))
    #     try:
    #
    #         # OMG, FIX ME!
    #         from playground.jobs.alpha import Alpha
    #         from playground.jobs.mock import Mock
    #
    #
    #         return eval(re.sub("\W", "", self.name).capitalize())
    #     except NameError as nameError:
    #         logger.error("Implementation for %s not found! %s" % (self.name, nameError))
    #         print("Implementation for %s not found! %s" % (self.name, nameError))
    #         return None

    def update_last_running_time_and_counter(self):
        the_last_detector_by_name = Detector.objects.get(name=self.name)
        the_last_detector_by_name.full_clean()
        # https://docs.djangoproject.com/en/1.4/topics/i18n/timezones/#naive-and-aware-datetime-objects
        the_last_detector_by_name.last_run_date = datetime.datetime.utcnow().replace(tzinfo=utc)
        the_last_detector_by_name.run_count = F('run_count') + 1
        the_last_detector_by_name.save()
        # Reload:
        return Detector.objects.get(name=self.name)

    def get_agent_mock(self):
        """
        :return: A Mock
        """
        from playground.agents.mock import Mock
        return Mock

class Result(models.Model):
    """
    Map in some way the Detector's results
    """
    detector = models.ForeignKey(Detector)
    content = models.CharField(max_length=1000)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField('creation date')
    processed = models.BooleanField(default=False)
    duration = models.IntegerField('seconds of processing', default=0)

    def was_created_recently(self):
        return self.creation_date >= timezone.now().replace(tzinfo=utc) - datetime.timedelta(hours=1)

    def __str__(self):
        return 'Result from {detector_name} is {content}'.format(
            detector_name=self.detector.name,
            content=self.content
        )
