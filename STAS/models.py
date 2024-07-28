from typing import Iterable
from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

def valid_phone_number_check(value):
    if len(value)<10:
        raise ValidationError("Phone Number should be atleast 10 digits")
    elif len(value)<=13:
        if value[:3]!="+91":
            raise ValidationError("Please provide a valid phone number")




class Test(models.Model):
    name=models.CharField(max_length=256)
    id=models.IntegerField
    email=models.CharField(max_length=100,default="test@Example.com")

class RecruitmentMaster(models.Model):
    candidate_name=models.CharField(max_length=256)
    experience=models.IntegerField(max_length=10)
    mobile_number=models.CharField(validators=[
        MinLengthValidator(10),
        MaxLengthValidator(13),
        # RegexValidator(r'^\+91\d{10}$'),
        valid_phone_number_check
    ]
    )
    profile_source = models.CharField( max_length=256,blank=True)
    slug=models.SlugField(default="",null=False,db_index=True)

    def save(self,*args, **kwargs): 
        self.slug=slugify(self.candidate_name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("candidate_detail", args=[self.slug])
    

    def __str__(self) -> str:
        return f"candidate_name={self.candidate_name} \t mobile_number=  {self.mobile_number}\n"



