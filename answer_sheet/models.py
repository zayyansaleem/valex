from django.db import models

# Create your models here.


class AnswerSheet(models.Model):
    answer_id = models.AutoField(primary_key=True)
    student_id = models.IntegerField()
    answer_sheet = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'answer_sheet'
