from django.urls import path,include
from users.views import *

urlpatterns = [

    path('',index,name = 'index'),
]
