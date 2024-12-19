from django.db import models
from student.models import Student

# Create your models here.


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'
