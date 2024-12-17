from django.db import models

# Create your models here.


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=100)
    attachment = models.CharField(max_length=450)


    class Meta:
        managed = False
        db_table = 'complaint'
