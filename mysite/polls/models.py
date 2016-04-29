
import datetime 

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

 

class AsimData(models.Model):
    trig = models.CharField(max_length=200)
    lev1 = models.CharField(max_length=200)
    lev2 = models.CharField(max_length=200)
    inst = models.CharField(max_length=200)
    prev = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()
    obsid = models.FloatField()
    obs_date = models.DateTimeField('date observed')
    def __str__(self):
        return self.question_text
