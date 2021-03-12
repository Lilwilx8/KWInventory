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
    path('sales', views.sales, name="Sales"),
    path('createSales', views.CreateSale, name="CreateSales"),
    path('editSale/<int:Id>', views.EditSale, name="EditSales"),
    path('deleteSale/<int:Id>', views.DeleteSale, name="DeleteSales"),
]