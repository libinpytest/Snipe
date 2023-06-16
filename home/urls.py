from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from home.views import homeland

urlpatterns = [
    path('', views.homeland),
    path('submit_message/', views.submit_message, name='submit_message'),
    path('', homeland, name='homeland'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('notifications/', views.notifications, name='notifications'),
    path('reset_message_count/', views.reset_message_count, name='reset_message_count'),
    path('logout/', views.logout_view, name='logout'),
]