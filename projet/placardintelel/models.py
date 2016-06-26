from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RECEPTION(models.Model):
    id = models.AutoField(primary_key=True)
    #tag = models.ForeignKey('REFERENCE_TAG',on_delete=models.CASCADE, default=0)
    masse = models.FloatField(default=0)
    date = models.IntegerField()
    def __unicode__(self):
        return str(self.masse)+" "+str(self.date);

class REFERENCE_TAG(models.Model):
    id_tag = models.TextField(primary_key=True)
    calories = models.FloatField()
    def __unicode__(self):
        return str(self.id_tag)+" "+str(self.calories);

class PRODUIT_PRESENT(models.Model):
    id_tag = models.IntegerField(primary_key=True)
    id_reception = models.IntegerField()
    def __unicode__(self):
        return str(self.id_tag)+" "+str(self.calories);
        
class MASSE_PRELEVEE(models.Model):
    id = models.AutoField(primary_key=True),
    id_tag = models.IntegerField()
    masse = models.FloatField()
    date = models.IntegerField()
    def __unicode__(self):
        return str(self.id_tag)+" "+str(self.date);

class MASSE_ACTUELLE(models.Model):
    id_tag = models.IntegerField()
    masse = models.FloatField()
    def __unicode__(self):
        return str(self.id_tag)+" "+str(self.masse);
