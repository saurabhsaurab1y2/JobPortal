from django.urls import path

from . import views


urlpatterns=[
    path("home/",views.home),
    path("index/",views.index),
    path("",views.index),
    path("contact/",views.contact),
    path("about/",views.about),
    path("gallery/",views.gallery),
    path("team/",views.team),
    path("profile/",views.profile),
    path("uprofile/",views.uprofile),
    path("registration/",views.registration),
    path("login/",views.login),
    path("dashboard/",views.dashboard),
    path("company/",views.company),
    path("jobs/",views.jobs),
    path("jobdetail/",views.jobdetail),
    path("apply/",views.apply),
    path("myjobs/",views.myjobs),
    path("delete/",views.delete),
    path("index/", views.index, name="index"),
    
    
    
    
]