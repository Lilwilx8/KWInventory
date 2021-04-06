from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib import admin

from .views import Products, UpdateProduct, DeleteProduct, AddProduct, Customers, AddCustomer, UpdateCustomer, \
    DeleteCustomer, Sales, AddSale, UpdateSale, DeleteSale

urlpatterns = [

    path('products', login_required(Products.as_view()), name='Products'),
    path('addProduct', login_required(AddProduct.as_view()), name='AddProduct'),
    path('updateProduct/<int:pk>', login_required(UpdateProduct.as_view()), name='UpdateProduct'),
    path('deleteProduct/<int:pk>', login_required(DeleteProduct.as_view()), name='DeleteProduct'),
    path('customers', login_required(Customers.as_view()), name="Customers"),
    path('addCustomer', login_required(AddCustomer.as_view()), name="AddCustomer"),
    path('updateCustomer/<int:pk>', login_required(UpdateCustomer.as_view()), name='UpdateCustomer'),
    path('deleteCustomer/<int:pk>', login_required(DeleteCustomer.as_view()), name="DeleteCustomer"),
    path('sales', login_required(Sales.as_view()), name="Sales"),
    path('addSale', login_required(AddSale.as_view()), name="AddSale"),
    path('updateSale/<int:pk>', login_required(UpdateSale.as_view()), name='UpdateSale'),
    path('deleteSale/<int:pk>', login_required(DeleteSale.as_view()), name="DeleteSale"),
    path('admin/', admin.site.urls),

]
