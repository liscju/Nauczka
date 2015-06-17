from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.TextField()
    url = models.TextField()

class Note(models.Model):
    course = models.ForeignKey("Course",default=None)
    time_spent = models.IntegerField(default=0)
    description = models.TextField(default='')