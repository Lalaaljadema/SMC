from django.db import models


class StudentData(models.Model):
    student_number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    field_of_study = models.CharField(max_length=255)
    GPA = models.FloatField()

    def __str__(self):
        return self.first_name
