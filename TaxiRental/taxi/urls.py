from django.urls import include ,path
from . import views

urlpatterns = [
   path("",views.index,name="HomePage"),
   path("contact/",views.contact, name="Contact Us"),
   path("dashboard/",views.dashboard,name="Dashboard"),
   path("signin/", views.sign_in, name="signin"),
   path("callback", views.callback, name="callback"),
   path("checkout/", views.checkout, name="Checkout"),
   path("handlerequest/", views.handlerequest, name="HandleRequest")
]