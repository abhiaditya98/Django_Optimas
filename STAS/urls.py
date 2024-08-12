from django.urls import path
from . import views

urlpatterns=[
    path("",views.HomePage,name="homepage"),
    path("all_candidates",views.all_candidates,name="all_candidates_url"),
    path("all_candidates/<slug:slug>",views.candidate_details, name="candidate_detail"),
    path("<int:page>",views.PageLoadedIsNumber),
    path("Recruiter/",views.candidate_details_submitted),
    # path("<str:page>",views.PageLoaded,name="applications"),
    path("Recruiter/thank-you",views.thank_you),
    
    
    # path("stas/1/",views.page)
]