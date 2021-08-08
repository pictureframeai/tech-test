from django.db import models
from datetime import datetime

class Photo(models.Model):
    image = models.ImageField(height_field=None, width_field=None, max_length=100, blank=True)
    dateTaken = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now, verbose_name='The date and time the photo was taken')
    takenBy = models.CharField(max_length=100, verbose_name='The person which has taken the photo')
    approvedDate = models.DateField(default=datetime.now)
    def __str__(self):
        return self.image.name
