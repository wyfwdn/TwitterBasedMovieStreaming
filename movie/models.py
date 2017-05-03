from __future__ import unicode_literals

from django.db import models

class table(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    result = models.TextField()
    neg = models.FloatField(max_length=100)
    neu = models.FloatField(max_length=100)
    pos = models.FloatField(max_length=100)
    def __unicode__(self):
        return self.name+self.content+self.result+self.pos+self.neu+self.neg

class age_gender(models.Model):
    age = models.TextField()
    gender = models.TextField()
    def __unicode__(self):
        return self.age+self.gender