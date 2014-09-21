from django.db import models

# Create your models here.

class OfficeHours(models.Model)
    DAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('R', 'Thursday'),
        ('F', 'Friday'),
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=1, choices=DAYS, unique=True)
    
    def __str__(self):
        return self.day
    


