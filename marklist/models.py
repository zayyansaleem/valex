from django.db import models
from student.models import Student
from application.models import Application

# Create your models here.



class Marklist(models.Model):
    marklist_id = models.AutoField(primary_key=True)
    # application_id = models.IntegerField()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    # student_id = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marklist = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'marklist'

