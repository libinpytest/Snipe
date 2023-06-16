from django.urls import path
from contact import views
from home.views import homeland

urlpatterns = [
    path("", views.contact),

]