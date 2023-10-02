from django.db import models
from uuid import uuid4


class ChapaStatus(models.TextChoices):
    CREATED = 'created', 'CREATED'
    PENDING = 'pending', 'PENDING'
    SUCCESS = 'success', 'SUCCESS'
    FAILED = 'failed', 'FAILED'


class ChapaTransactionMixin(models.Model):
    "inherit this model and add your own extra fields"
    id = models.UUIDField(primary_key=True, default=uuid4)

    amount = models.FloatField()
    currency = models.CharField(max_length=25, default='ETB')
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    payment_title = models.CharField(max_length=255, default='Payment')
    description = models.TextField()

    status = models.CharField(max_length=50, choices=ChapaStatus.choices, default=ChapaStatus.CREATED)

    response_dump = models.JSONField(default=dict, blank=True)  # incase the response is valuable in the future
    checkout_url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.first_name} - {self.last_name} | {self.amount}"
    
    def serialize(self) -> dict:
        return {
            'amount': self.amount,
            'currency': self.currency,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'description': self.description
        }

class ChapaTransaction(ChapaTransactionMixin):
    pass
