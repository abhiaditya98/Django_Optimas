from django.urls import path
from . import views

urlpatterns=[
    path("",views.HomePage,name="homepage"),
    path("<int:page>",views.PageLoadedIsNumber),
    path("<str:page>",views.PageLoaded,name="applications"),
    
    
    # path("stas/1/",views.page)
]