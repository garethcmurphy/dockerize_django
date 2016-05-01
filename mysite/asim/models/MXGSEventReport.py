from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
import datetime
from django.contrib import admin

class MXGSEventReport (models.Model):
    packet_length                   = models.IntegerField('Packet length')
    INFORMATION = "INF"
    ADVISORY = "ADV"
    CAUTION = "CAU"
    WARNING = "WAR"
    EMERGENCY = "EME"
    EVENT_SEVERITY_CHOICES = (
        (INFORMATION, "Information"),
        (ADVISORY, "Advisory"),
        (CAUTION, "Caution"),
        (WARNING, "Warning"),
        (EMERGENCY, "Emergency")
    )
    event_severity = models.CharField(max_length=3,
                                         choices=EVENT_SEVERITY_CHOICES,
                                         default=INFORMATION)
    
    event_id                        = models.IntegerField()
    utc_year                        = models.IntegerField('UTC year')
    utc_msec                        = models.IntegerField('UTC msec')
    utc_seconds                     = models.IntegerField('UTC seconds')

