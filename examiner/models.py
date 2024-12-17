from django.db import models

# Create your models here.


class Examiner(models.Model):
    examiner_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    experience = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    phone_number = models.CharField(db_column='phone number', max_length=45)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'examiner'

