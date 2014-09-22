from django.db import models

# Create your models here.

class OfficeHours(models.Model)
    DAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.SmallPositiveIntegerField(max_length=1, choices=DAYS, unique=True)
    
    def __str__(self):
        return self.day
    
    class Meta:
        ordering = ['day']


