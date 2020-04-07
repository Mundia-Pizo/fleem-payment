from django.urls import path
from .views import HomeView, BalanceView, MoneyTransCreatView,MoneyTransferDetailView

urlpatterns=[
   path('',HomeView.as_view(), name="home"),
   path('balance/', BalanceView.as_view(), name="balance"),
   path('money-transfer/new/',MoneyTransCreatView.as_view(), name="money-transfer" ),
   path('money-transfer-detail/<int:pk>/',MoneyTransferDetailView.as_view(), name="transfer-detail")
#    path('transfers/', MoneyTransferView.as_view(), name="transfers")
]