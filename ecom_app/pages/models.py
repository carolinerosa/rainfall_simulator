from django.db import models

class Bacia(models.Model):
    idcodsubbacia = models.IntegerField()
    codsubbacia = models.CharField(max_length=50)
    nombacia = models.CharField(max_length=50)
    nomsubbacia = models.CharField(max_length=50)
    numlatitude = models.FloatField()
    numlongitude = models.FloatField()
    def __str__(self):
        return self.nombacia
    class Meta:
      app_label = 'bacia'
      db_table = 'tb_depara_ecmwf'
      managed = False