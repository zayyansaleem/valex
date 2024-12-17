from django.db import models

# Create your models here.


class Doubts(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    doubt = models.CharField(max_length=100)
    response = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'doubts'
