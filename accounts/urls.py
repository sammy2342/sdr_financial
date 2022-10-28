from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from banking import admin

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
