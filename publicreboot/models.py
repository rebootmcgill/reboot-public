from django.db import models

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
        return "{1}-{2:d}".format(str(name), start_date.year)
