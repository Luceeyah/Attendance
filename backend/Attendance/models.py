
from django.db import models
from django.utils import timezone


# Create your models here.
class Attendance(models.Model):
    # staff_Id= models.PositiveIntegerField(null=True)
    name= models.CharField(max_length=100,null=True)
    created_at=models.DateField(auto_now_add=True, null=True,blank=True)
    gender= models.CharField(max_length=30,null=True)
    designation=models.CharField(max_length=30,null=True,blank=True)
    email= models.EmailField(max_length=100,null=True)
    # phone_number=models.PhoneNumberfield()
    total_leave_days=models.PositiveIntegerField(null=True,blank=True)
    casual_leave_days=models.PositiveIntegerField(null=True,blank=True)
    # events=models.DateTimeField(max_length=100,null=True,blank=True)


    def __str__(self) :
        return self.name

