# urls.py
from django.urls import path
from . import views


urlpatterns = [
    
    path('create-reminder/', views.create_reminder, name='create_reminder'),
]
