from django.db import models
from student.models import Student

# Create your models here.


class AnswerSheet(models.Model):
    answer_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    answer_sheet = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'answer_sheet'
