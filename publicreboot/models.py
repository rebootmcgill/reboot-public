from django.db import models
from django.utils import timezone

# Create your models here.

class OfficeHours(models.Model):
    DAYS = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.PositiveSmallIntegerField(choices=DAYS, unique=True)
    closed = models.BooleanField(default=True)
    
    def get_day(self):
        return str(self.DAYS[self.day-1][1])
    
    def __str__(self):
        return self.get_day() + ' ' + str(self.start_time) + ' - ' + str(self.end_time)
    
    class Meta:
        ordering = ['day']


class Holiday(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{0}-{1:d}".format(str(self.name), self.start_date.year)

    def active(self):
        today = timezone.now()
        return today > self.start_date and today < self.end_date
    active.short_description = 'Current Holiday'
    active.boolean = True

    def future(self):
        return timezone.now() > self.end_date
    future.short_description = 'Future Holiday'
    future.boolean = True

    def past(self):
        return timezone.now() < self.start_date
    past.short_description = 'Past Holiday'
    past.boolean = True
