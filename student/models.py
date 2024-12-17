from django.db import models

# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    department = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(unique=True, max_length=45)
    address = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'student'
