from django.db import models

class Laborer(models.Model):
    lab_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dist_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'laborer'

class Supervisor(models.Model):
    sup_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'supervisor'
