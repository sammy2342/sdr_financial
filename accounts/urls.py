from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
=======
    path('login/', auth_views.LoginView.as_view(), name='login'),
>>>>>>> main
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
