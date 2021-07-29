from django.urls import path
from . import views

app_name = 'duties'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('get/user/<str:username>/', views.get_users, name='get_users'),
    path('get/duties/<str:username>/', views.get_user_duties, name='get_user_duties'),
]
