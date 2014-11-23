from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin


class Entry(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
            return unicode(self.creator) + u" - " + (self.title)


    class Meta:
        verbose_name_plural = "entries"
