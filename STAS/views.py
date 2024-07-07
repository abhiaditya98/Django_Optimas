from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

applications={
     "recruiter":"This is the Recruiter page",
     "HM":"This is the HM Page",
}
def index(request):
    return HttpResponse("This is 1st django application which I'm created its looking pretty cool...\
                       isn't it ")

def PageLoadedIsNumber(request,page):
        if page==1:
             url_app=reverse("applications",args=[page])        
        elif page==2:
            url_app=reverse("applications",args=[page])
        return HttpResponseRedirect(url_app) 

'''This is using the render method'''
def PageLoaded(request,page):
     try:
        app_name=page
        #   response_data=applications[app_name]
        # response_data = render_to_string("STAS/stas.html") #old way
          #a better way to do it is

        return render(request,"STAS/stas.html",{
             "app_page":applications[app_name]
        })
        '''Note to myself here we have given the app name inside the templates folder cause django load all the templates in folder if any other app has the same html or template file the it will be crashed so it's best practise to have the app name included in it.'''
     
     
     except Exception as e:
          return HttpResponseNotFound(f"The {e} application is yet to build ")      
'''Without the template default page to be loaded'''       
def PageLoaded(request,page):
    for key,values in applications.items():
        # return HttpResponse(key)
        if page==key:
            return HttpResponse(applications[key]) 
        elif page==key:
            return HttpResponse(applications[key]) 
    else:
        return HttpResponseNotFound(f"The exception {page} ")    
'''Using the HTML Template'''
# def PageLoaded(request,page):
#      sel=request.path.strip()
#      return HttpResponse(sel)
#      selectedpage=page
#      context={
#         #   "applications":applications,
#           "selectedpage":selectedpage
#         }
#      return render(request,"STAS/stas.html",context)


'''Restructring the Home Page'''
# def HomePage(request):
#     list_of_applications_list=""
#     for key,val in applications.items():
#         url_path=reverse("applications",args=[key])
#         list_of_applications_list += f"<li><a href =\"{url_path}\"> {key}</a></li>"
#         response_data=f"<ul>{list_of_applications_list}</ul>"
    
            
#     return HttpResponse(response_data)
'''Using the html template'''
          
def HomePage(request):
    context = {'applications': applications}
    return render(request, "STAS/homepage.html", context)