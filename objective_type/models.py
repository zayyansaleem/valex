from django.db import models

# Create your models here.


class ObjectiveType(models.Model):
    objective_id = models.AutoField(primary_key=True)
    question_paper = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'objective_type'
