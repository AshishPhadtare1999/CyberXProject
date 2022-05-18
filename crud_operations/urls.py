from math import frexp
from django.urls import path
from crud_operations.views import *

urlpatterns = [
    path('',show,name="display"),
    path('delete/<int:id>',delete_cust,name="delete"),
    path('update/<int:id>',update_data,name="update")
]
