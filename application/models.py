from django.db import models
from student.models import Student
from schedule.models import Schedule


# Create your models here.


class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # schedule_id = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'application'
