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
    
    def __str__(self):
        return str(DAYS[self.day-1][1]) + ' ' + str(self.start_time) + ' - ' + str(self.end_time)
    
    class Meta:
        ordering = ['day']


