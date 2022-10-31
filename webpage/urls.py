from django.urls import path
from webpage.views import *

app_name = 'webpage'

urlpatterns = [
    path('', index_view, name='index'),
]
