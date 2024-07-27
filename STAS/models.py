from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator,MaxLengthValidator
# Create your models here.


class Test(models.Model):
    name=models.CharField(max_length=256)
    id=models.IntegerField
    email=models.CharField(max_length=100,default="test@Example.com")

class RecruitmentMaster(models.Model):
    candidate_name=models.CharField(max_length=256)
    experience=models.IntegerField
    mobile_number=models.CharField(max_length=13,validators=[
        MinLengthValidator(10),
        MaxLengthValidator(13),
        RegexValidator(r'^\+91\d{10}$')
    
    ]
    )
    profile_source = models.CharField( max_length=256)



