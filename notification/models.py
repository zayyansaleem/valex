from django.db import models

# Create your models here.


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'notification'

