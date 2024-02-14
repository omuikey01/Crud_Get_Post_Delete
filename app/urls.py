from django.urls import path
from .views import *


urlpatterns = [
    path("", homepage, name=""),
    path("form/", formfun, name="form"),
    path("show/", showfun, name="show"),
    path("delete/", deleteFun, name="delete"),
]
