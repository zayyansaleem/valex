from django.db import models

# Create your models here.



class Marklist(models.Model):
    marklist_id = models.AutoField(primary_key=True)
    application_id = models.IntegerField()
    student_id = models.IntegerField()
    marklist = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'marklist'

