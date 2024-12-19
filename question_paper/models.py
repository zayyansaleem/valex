from django.db import models
from schedule.models import Schedule
# Create your models here.


class QuestionPaper(models.Model):
    question_id = models.AutoField(primary_key=True)
    # schedule_id = models.IntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    question_paper = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'question_paper'
