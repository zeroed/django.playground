# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


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

    @staticmethod
    def get_mock():
        obj, created = Detector.objects.get_or_create(
            name='Mock',
            description='Mock Detector'
        )
        return obj


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


class Taskmeta(models.Model):
    """
    Get the results from the DB (raw) ...
    """
    id = models.IntegerField(primary_key=True)
    task_id = models.CharField(unique=True, max_length=255, blank=True)
    status = models.CharField(max_length=50, blank=True)
    result = models.BinaryField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    traceback = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'foobardb_taskmeta'
