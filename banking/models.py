from email.policy import default
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
ACCOUNT_TYPES = (
    ('C', 'Checkings'),
    ('S', 'Savings'),
)
TRANSACTION_TYPES = (
    ('W', 'Withdraw'),
    ('D', 'Deposit'),
    ('P', 'Purchase')
)


class Account(models.Model):
    number = models.CharField(max_length=100)
    balance = models.IntegerField()
    type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPES,
        default=ACCOUNT_TYPES[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.number} ({self.user.username})'


class Transaction(models.Model):
    date = models.DateField('Transaction Date')
    amount = models.IntegerField()
    remaining_balance = models.IntegerField(null=True)
    description = models.TextField(max_length=12)
    type = models.CharField(
        max_length=1,
        choices=TRANSACTION_TYPES,
        default=TRANSACTION_TYPES[0][0]
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description  } on {self.date}'

    class Meta:
        ordering = ['-created_at']
