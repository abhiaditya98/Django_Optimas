from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse("This is 1st django application which I'm created its looking pretty cool...\
                       isn't it ")

def PageLoadedIsNumber(request,page):
        if page==1:

            return HttpResponseRedirect("recruiter")
        
        elif page==2:
             url_app=reverse("applications",args=[page])
             return HttpResponseRedirect("HM") 

def PageLoaded(request,page):
    if page=="recruiter":
        loaded_page=page 
        
    elif page=="HM":
        loaded_page=page

    else:
        return HttpResponseNotFound(f"This URL specified {page} is incorrect")
    
    return HttpResponse("This is  the STAS {0} page".format(loaded_page))
