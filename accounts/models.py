from django.db import models
from django.contrib.auth import get_user_model
from  django.conf import settings

User=get_user_model()
class PersonalAccount(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email     = models.EmailField()
	phone     = models.IntegerField(blank=True, null=True)


	def __str__(self):
		return f"{self.first_name} {self.last_name}"

BUSINESS_ACCOUNT_CHOICES=(
    ('ts','Test Account'),
    ('bs','Busines Account')
	)
class BusinessAccount(models.Model):
	owner        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	account_name = models.CharField(max_length=50)
	account_type = models.CharField(max_length=2,
	 choices=BUSINESS_ACCOUNT_CHOICES,default='Test Account')
	business_owner=models.ForeignKey(PersonalAccount,on_delete=models.CASCADE,null=True, default=User)
	business_location= models.CharField(max_length=300,blank=True)
	busines_email    = models.EmailField(blank=True)
	secret_key       = models.CharField(max_length=100,blank=True)

	def __str__(self):
		return f"{self.account_name}"




