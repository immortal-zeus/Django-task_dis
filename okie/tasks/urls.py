from django.urls import path, include
from . import views

urlpatterns=[
    path("" , views.index, name="index"),
    path("signin", views.signin , name="signin" ),
    path("login", views.login , name="login"),
    path("logout", views.logout , name="logout"),
    path("taskcreation", views.task_creation , name="creation"),
    path("taskdisplay", views.task_display , name="display"),
    path("zzincrezz", views.increase , name="inc")
]