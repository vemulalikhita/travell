
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Tour(models.Model):
    first_name = models.CharField(max_length=250)
    image = models.FileField(null=True, blank=True)
    content = models.TextField(max_length=1000)
    #description = models.TextField(max_length=1000)

    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def _unicode_(self):
        return self.first_name

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("mysite:detail", kwargs={"id":self.id})
        #return "/mysite/%s/" %(self.id)

class Tourist(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
   # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def _unicode_(self):
        return self.name

    def __str__(self):
        return self.name

