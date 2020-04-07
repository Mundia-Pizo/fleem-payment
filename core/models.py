from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class MoneyTransfer(models.Model):
	sender   = models.ForeignKey(settings.AUTH_USER_MODEL,default=User, on_delete=models.CASCADE)
	receiver = models.EmailField(unique=False)
	amount   = models.IntegerField(default=0)
	date     = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.sender} sent ${self.amount} to {self.receiver}"

	def get_absolute_url(self,*args, **kwargs):
		return reverse('transfer-detail', kwargs={'pk':self.pk})
	def get_amount(self):
		return self.amount

class Balance(models.Model):
	transfers   = models.ManyToManyField(MoneyTransfer)  
	amount_deposited  = models.IntegerField(default=0)
	net_amount        = models.IntegerField(default=0)
	user              = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Net amount :k{self.net_amount}"

	def get_total_balance(self, *args, **kwargs):
		total = 0    
		for transfer in self.transfers.all():
			total +=transfers.get_amount()
		return total
			
class Payment(models.Model):
	merchandise_name = models.CharField(max_length=200)
	amount_paid      = models.IntegerField()
	balance          = models.ManyToManyField(Balance)
	user             = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f"Payment to {self.merchandise_name}"

	def get_total_balance(self):
		total = 0

		for balance in self.balance.all():
			total+=balance
			return total
		return total


class Deposit(models.Model):
	account_name     = models.CharField(max_length=200)
	account_number   = models.IntegerField()
	amount_deposited = models.IntegerField()
	date             = models.DateTimeField()

	def __str__(self):
		return f"Cash Deposit {self.account_name} @{self.date}"


class VisaDetails(models.Model):
	account_holder = models.CharField(max_length=150)
	visa_card_number=models.IntegerField()
	CSV_number      = models.IntegerField()

	def __str__(self):
		return self.account_holder