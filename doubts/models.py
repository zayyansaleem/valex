from django.db import models
from student.models import Student

# Create your models here.


class Doubts(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    doubt = models.CharField(max_length=100)
    response = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'doubts'
