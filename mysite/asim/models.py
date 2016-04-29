from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class ScienceData(models.Model):
    lat=models.FloatField('Latitude')
    lon=models.FloatField('Longitude')
    obsid=models.IntegerField('ObservationId')
    date=models.DateTimeField('Date Observed')
    trig=models.CharField(max_length=200)
    inst=models.CharField(max_length=200)
    lev0=models.CharField(max_length=200)
    lev1=models.CharField(max_length=200)
    prev=models.CharField(max_length=200)
    def __str__(self):
        return 'Lat: '+str(float(self.lat))+' , Lon: '+str(float(self.lon))+' , ObsId: '+str(int(self.obsid))
 
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Mmia(models.Model):
    lat=models.FloatField('Latitude')
    lon=models.FloatField('Longitude')
    obsid=models.IntegerField('ObservationId')
    date=models.DateTimeField('Date Observed')
    trig=models.CharField(max_length=200)
    inst=models.CharField(max_length=200)
    lev0=models.CharField(max_length=200)
    lev1=models.CharField(max_length=200)
    prev=models.CharField(max_length=200)
    chu1prev=models.CharField(max_length=200)
    chu2prev=models.CharField(max_length=200)
    phot1prev=models.CharField(max_length=200)
    phot2prev=models.CharField(max_length=200)
    phot3prev=models.CharField(max_length=200)
    def __str__(self):
        return 'Lat: '+str(float(self.lat))+' , Lon: '+str(float(self.lon))+' , ObsId: '+str(int(self.obsid))
 
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

class MonitoredHousekeeping(models.Model):
    alivecnt=models.FloatField('Alive Counter')
    bootstat=models.FloatField('Boot status')
    swmode=models.FloatField('SW mode')
    errors=models.FloatField('Errors/Warnings ')
    temper=models.FloatField('Temperature 1')
    tmcnt=models.FloatField('TM count ')
    tccnt=models.FloatField('TC count ')
	


class InstrumentHousekeeping(models.Model):
    swmode=models.FloatField('SW mode')
    errors=models.FloatField('Errors/Warnings ')
    temp1=models.FloatField('Temperature 1')
    tmcnt=models.FloatField('TM count ')
    tccnt=models.FloatField('TC count ')
    inston=models.FloatField('Inst ON/OFF')
    hvolt=models.FloatField('Hvolt')
    daylight=models.FloatField('Day light sensor')
    triggers=models.FloatField('Triggers/Priority')
	

class CHUHousekeeping(models.Model):
    swmode=models.FloatField('SW mode')

class PHOTHousekeeping(models.Model):
    swmode=models.FloatField('SW mode')
	
