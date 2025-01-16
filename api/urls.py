from django.urls import path
from expense import views
urlpatterns = [
    path('transaction',views.Transactions.as_view()),
    path('get-transaction',views.get_transaction)
]
