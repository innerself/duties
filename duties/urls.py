from django.urls import path
from . import views

app_name = 'duties'

urlpatterns = [
    path('', views.login, name='login'),
]
