from .models import Payment, MoneyTransfer, Balance,Deposit
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db.auth.models import User


@receiver(post_save, sender=User):
def 

