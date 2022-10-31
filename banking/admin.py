from django.contrib import admin
from .models import Account, Transaction

# Register your models here.
admin.site.register([Account, Transaction])
