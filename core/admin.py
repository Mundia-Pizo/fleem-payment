from django.contrib import admin

from .models import MoneyTransfer, Balance, Payment

admin.site.register(Balance)
admin.site.register(MoneyTransfer)
admin.site.register(Payment)



