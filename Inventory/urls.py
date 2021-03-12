from django.urls import path
from Inventory import views

urlpatterns = [
    path('products', views.products, name="Products"),
    path('createProducts', views.CreateProduct, name="CreateProducts"),
    path('editProduct/<int:Id>', views.EditProduct, name="EditProducts"),
    path('deleteProduct/<int:Id>', views.DeleteProduct, name="DeleteProducts"),
    path('customers', views.customers, name="Customers"),
    path('createCustomers', views.CreateCustomer, name="CreateCustomers"),
    path('editCustomer/<int:Id>', views.EditCustomer, name="EditCustomers"),
    path('deleteCustomer/<int:Id>', views.DeleteCustomer, name="DeleteCustomers"),

]