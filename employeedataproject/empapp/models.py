from django.db import models
class EmployeeData(models.Model):
       first_name=models.CharField(max_length=50)
       last_name=models.CharField(max_length=50)
       email=models.EmailField(max_length=50)
       location=models.CharField(max_length=50)
       salary=models.IntegerField()
       job=models.CharField(max_length=50)
       company=models.CharField(max_length=50)
       address=models.CharField(max_length=200)
