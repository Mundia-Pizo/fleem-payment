from rest_framework import serializers
from .models import Payment, Balance, MoneyTransfer

class BalanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Balance
		fields=[
		'net_amount']


class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Payment
		fields=[
		'merchandise_name', 'amount_paid']

class MoneyTrasnferSerializer(serializers.ModelSerializer):
	class Meta:
		model=MoneyTransfer
		fields=[
         'sender', 'receiver','amount', 'date'
		]