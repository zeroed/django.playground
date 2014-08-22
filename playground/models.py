# Create your models here.
import time
import datetime
from django.db import models, IntegrityError
from django.utils import timezone
from django.db import transaction


class Detector(models.Model):
    """
    The single detector
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default=None, blank=True, null=True)
    last_run_date = models.DateTimeField('last run date', default=None, blank=True, null=True)
    run_count = models.IntegerField('run count', default=0)
    created_at = models.DateTimeField('date created', default=datetime.datetime.utcnow())

    def was_runned_recently(self):
        return self.last_run_date >= timezone.now() - datetime.timedelta(hours=1)

    def __str__(self):
        return 'Detector {name}, "{description}" - last run: {last_run}'.format(
            name=self.name,
            description=self.description,
            last_run=self.last_run_date
        )

    def do_something(self, x, y, d):
        self.update_last_running_time_and_counter()
        time.sleep(d)
        return x + y

    @classmethod
    @transaction.atomic
    def get_mock(cls):
        try:
            # https://docs.djangoproject.com/en/1.6/releases/1.6.3/#select-for-update-requires-a-transaction
            with transaction.atomic():
                # https://docs.djangoproject.com/en/1.6/ref/models/querysets/#select-for-update
                detector_found_or_created = Detector.objects.select_for_update().filter(name='Mock').first()
                print('\n\n\nfound %s\n\n\n' % detector_found_or_created)
                if not detector_found_or_created.id:
                    detector_found_or_created = Detector.objects.create(
                        name='Mock',
                        description='Mock Detector'
                    )
                return detector_found_or_created
        except IntegrityError:
            print('fuuuuuuuuuuuuuuuuuuuu')


    def update_last_running_time_and_counter(self):
        self.full_clean()
        self.last_run_date = datetime.datetime.utcnow()
        self.run_count += 1
        self.save()
        return self


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
        return self.creation_date >= timezone.now() - datetime.timedelta(hours=1)

    def __str__(self):
        return 'Result from {detector_name} is {content}'.format(
            detector_name=self.detector.name,
            content=self.content
        )
