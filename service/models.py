from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=30)
    email_id=models.CharField(max_length=30)
    subject=models.CharField(max_length=30)
    mob_num=models.IntegerField()
    message=models.TextField(max_length=30)

class Department(models.Model):
    department_name=models.CharField(max_length=150)

    def __str__(self):
        return self.department_name

class DoctorDetails(models.Model):
    department_name=models.ForeignKey(Department, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    email_id=models.CharField(max_length=100)
    mobile_number=models.CharField(max_length=100)
    edu=models.CharField(max_length=100)
    department_desc=models.TextField(null=True)
