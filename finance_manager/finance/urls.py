from django.urls import path
from . import views

urlpatterns = [
    path('',views.transaction_list, name="transaction_list"),
    path('add/',views.add_transaction),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
]

