from django.urls import path
from Inventory import views

urlpatterns = [
    path('products', views.products, name="Products"),

]