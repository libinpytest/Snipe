from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contact/', include('contact.urls')),
    path('login/', include('login.urls')),
    path('services/', include('services.urls')),
    path('products/', include('products.urls')),
    path('', include('posts.urls')), 
]
