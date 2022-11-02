from django.urls import path
from . import views


urlpatterns = [
    path('account/create/', views.create_new_account, name='new_bank_account'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('transaction_delete/<int:account_id>/<int:pk>/', views.delete_transaction, name="delete_transaction")

]
