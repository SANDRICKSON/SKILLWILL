from django.urls import path
from . import views
from .views import profile_view

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/confirm/delete/', views.post_delete, name='confirm_delete'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('profile/<str:username>/', profile_view, name='profile'),

]
