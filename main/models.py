from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
# Create your models here.
class logIn(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=128)



class course(models.Model):
    COURSE_CHOICES = [
        ("PYTHON","python"),
        ("JAVA","java"),
        ("DOTNET","dotnet"),
        ("DJANGO","django"),
        ("REACT","react"),
    ]
    course_name = models.CharField(max_length=100,unique=True,default="PYTHON",choices=COURSE_CHOICES)
    

class register(models.Model):
    GENDER_CHOICES =[
        ("M","male"),
        ("F","female"),
        ("O","other"),
    ]
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    email = models.EmailField(unique=True, null=True, blank=True)
    dob = models.DateField(null=True,blank=True)
    age = models.PositiveSmallIntegerField(default=16,
        validators= [MinValueValidator(16),MaxValueValidator(40)]
    )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default="")
    mobile_no = models.CharField(max_length=20,default="")
    image = models.ImageField(null=True,blank=True)
    course = models.ForeignKey(course,on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=100,default="")
    address = models.CharField(max_length=255,default="none-address")
    reg_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
