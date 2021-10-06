
from django.urls import path
from .views import chart_select_view,add_purchase,sales_view

app_name = "products"

urlpatterns = [
   path('' ,chart_select_view , name="chart_select_view"),
   path('add_purchase/',add_purchase , name="add_purchase"),
   path('sales/',sales_view , name="sales_view"),
]