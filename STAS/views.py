from django.shortcuts import render
from models import RecruitmentMaster

valid_number="+911234567890"

try:
    valid_instance=RecruitmentMaster(mobile_number=valid_number)
    valid_instance.save()
    print(f"{valid_number} is a valid number")
except Exception as e:
    print(e)

# Create your views here.


