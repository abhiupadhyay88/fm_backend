from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255)
    contact_business_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    business_type = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    updation_time = models.DateTimeField()


    class Meta:
        db_table = 'facility'
        verbose_name = 'facility'

    def save(self, *args, **kwargs):
        self.updation_time = datetime.now()
        super(Facility, self).save(*args, **kwargs)