
from django.urls import path
from .views import customer_view

app_name = "customers"

urlpatterns = [
   path('' ,customer_view , name="customer_view"),
   
]