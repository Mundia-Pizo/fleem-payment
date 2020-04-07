from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView
from .models import MoneyTransfer, Balance, Payment


class HomeView(ListView):
    model = MoneyTransfer
    template_name = 'core/home.html'
    context_object_name ="moneytransfer_list"
    ordering =['-date']
    
    
class BalanceView(ListView):
    model = Balance
    template_name = 'core/balance.html'
    context_object_name="balance"
    

class MoneyTransCreatView(CreateView):
	model = MoneyTransfer
	fields=['receiver', 'amount']
	template_name = 'core/money-transfer.html'

	def form_valid(self, form):
		form.instance.sender=self.request.user
		return super().form_valid(form)

class MoneyTransferDetailView(DetailView):
	model = MoneyTransfer
	template_name = 'core/detail.html'
	context_object_name='transfer'

































































































# from rest_framework.views import APIView

# from .serializers import (
# 	PaymentSerializer, 
# 	BalanceSerializer, 
# 	MoneyTrasnferSerializer)

# from .models import Payment, MoneyTransfer, Balance
# from rest_framework.response import Response



# class PaymentView(APIView):
# 	def get(self,request, *args, **kwargs):
# 		qs = Payment.objects.all()
# 		serializer = PaymentSerializer(qs, many=True)
# 		return Response(serializer.data)


# 	def post(self, request, *args, **kwargs):
# 		serializer=PaymentSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		else:
# 			return Response(serializer.errors)

# class BalanceView(APIView):
# 	def get(self,request, *args, **kwargs):
# 		qs  =Balance.objects.all()
# 		serializer=BalanceSerializer(qs,many=True)
# 		return Response(serializer.data)

# class MoneyTransferView(APIView):
# 	def get(self, request, *args, **kwargs):
# 		qs= MoneyTransfer.objects.all()
# 		serializer= MoneyTrasnferSerializer(qs, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, *args, **kwars):
# 		serializer =MoneyTrasnferSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		else:
# 			return Response(serializer.errors)

