from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="HomePage"),
   path("info/",views.info,name="Information"),
   path("contact/",views.contact, name="Contact Us")
]