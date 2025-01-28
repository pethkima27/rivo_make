from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('produto/<int:produto_id>/', views.sale, name='sale'),
    path('login/', views.login_view, name='login'),
    path('', views.menu, name='menu'),
    path('register/', views.register, name='register'),
]
