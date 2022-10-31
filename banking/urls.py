from django.urls import path
from . import views


urls = [
    path('account/create/', views.create_account, name='new_bank_account'),
    path('dashboard', views.dashboard, name='dashboard')
]
