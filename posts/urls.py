from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post_view, name='create_post'),
    path('update/<int:post_id>/', views.update_post_view, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
    path('<int:post_id>/', views.view_post_detail, name='view_post_detail'),
    path('posts/', views.list_posts, name='posts'),
]
