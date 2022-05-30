from django.urls import path,include
from api.views import *

urlpatterns = [


#######################  Admin #######################################
#web urls  home
path('',index),
path('GetData',GetData.as_view()),


]