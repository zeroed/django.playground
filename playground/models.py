# Create your models here.
import threading
import time
import datetime
from django.db import models, IntegrityError
from django.utils import timezone
from django.db import transaction
from django.db.models import F
from celery.utils.log import get_task_logger
from django.utils.timezone import utc

logger = get_task_logger(__name__)


class Detector(models.Model):
    """
    The single detector
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    last_run_date = models.DateTimeField('last run date', default=None, blank=True, null=True)
    run_count = models.IntegerField('run count', default=0)
    created_at = models.DateTimeField('date created', default=datetime.datetime.utcnow())

    def was_runned_recently(self):
        return self.last_run_date >= timezone.now().replace(tzinfo=utc) - datetime.timedelta(hours=1)

    def __str__(self):
        return 'Detector {name}, "{description}" - last run: {last_run}'.format(
            name=self.name,
            description=self.description,
            last_run=self.last_run_date
        )

    @transaction.atomic()
    def do_something(self, x, y, d):
        with transaction.atomic():
            self.update_last_running_time_and_counter()
            time.sleep(d)
            return x + y

    @classmethod
    @transaction.atomic
    def get_mock(cls):
        """
        Get or create but for the poor-man-thread-safe version

        :return:
        """
        try:
            # https://docs.djangoproject.com/en/1.6/releases/1.6.3/#select-for-update-requires-a-transaction
            with transaction.atomic():
                # https://docs.djangoproject.com/en/1.6/ref/models/querysets/#select-for-update
                try:
                    detector_found_or_created = Detector.objects.get(name='Mock')
                except Detector.DoesNotExist:
                    detector_found_or_created = None
                if not detector_found_or_created:
                    logger.info('Creating Mock from %s' % threading.current_thread())
                    detector_found_or_created = Detector.objects.create(
                        name='Mock',
                        description='Mock Detector'
                    )
                return detector_found_or_created
        except IntegrityError as not_thread_safe_as_expected:
            logger.error('Some trivial concurrency problem occured here, ya know... %s' % not_thread_safe_as_expected)
            return Detector.objects.filter(name='Mock').first()

    def update_last_running_time_and_counter(self):
        the_last_detector_by_name = Detector.objects.get(name=self.name)
        the_last_detector_by_name.full_clean()
        # https://docs.djangoproject.com/en/1.4/topics/i18n/timezones/#naive-and-aware-datetime-objects
        the_last_detector_by_name.last_run_date = datetime.datetime.utcnow().replace(tzinfo=utc)
        the_last_detector_by_name.run_count = F('run_count') + 1
        the_last_detector_by_name.save()
        # Reload:
        return Detector.objects.get(name=self.name)


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
