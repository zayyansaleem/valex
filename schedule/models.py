from django.db import models

# Create your models here.


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=45)
    exam_date = models.DateField()
    exam_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule'
