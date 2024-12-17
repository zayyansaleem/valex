from django.db import models

# Create your models here.


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    schedule_id = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'application'
