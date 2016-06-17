from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HISTORIQUE_RECEPTIONS(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.ForeignKey('REFERENCE_TAG',on_delete=models.CASCADE, default=0)
    masse = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return str(self.id)+" "+str(self.date);

class REFERENCE_TAG(models.Model):
    id_tag = models.TextField(primary_key=True)
    calories = models.FloatField()
    def __unicode__(self):
        return str(self.id_tag)+" "+str(self.calories);


class MASSE_PRELEVEE(models.Model):
    id = models.AutoField(primary_key=True),
    tag = models.ForeignKey('REFERENCE_TAG',on_delete=models.CASCADE)
    masse = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return str(self.id)+" "+str(self.date);

class MASSE_ACTUELLE(models.Model):
    tag = models.ForeignKey('REFERENCE_TAG',on_delete=models.CASCADE)
    masse = models.FloatField()
    def __unicode__(self):
        return str(self.tag)+" "+str(self.masse);
