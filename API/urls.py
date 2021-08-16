from django.urls import path, include
from . import api
app_name='API'
urlpatterns = [
    path('', api.index, name='index'),
    path('get_data', api.get_data,name='get_data'),
  
]
