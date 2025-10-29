# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    compid = models.IntegerField(null=True, blank=True)
    compname = models.CharField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Vehicle(models.Model):

    #__Vehicle_FIELDS__
    vid = models.IntegerField(null=True, blank=True)
    compid = models.ForeignKey(company, on_delete=models.CASCADE)
    reg = models.CharField(max_length=255, null=True, blank=True)
    nextwash = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Vehicle_FIELDS__END

    class Meta:
        verbose_name        = _("Vehicle")
        verbose_name_plural = _("Vehicle")


class Washrecord(models.Model):

    #__Washrecord_FIELDS__
    vid = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    washtype = models.TextField(max_length=255, null=True, blank=True)
    washdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Washrecord_FIELDS__END

    class Meta:
        verbose_name        = _("Washrecord")
        verbose_name_plural = _("Washrecord")



#__MODELS__END
