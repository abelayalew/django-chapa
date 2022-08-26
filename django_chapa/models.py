from django.db import models
from uuid import uuid4


class ChapaStatus(models.TextChoices):
    PENDING = 'pending', 'PENDING'
    SUCCESS = 'success', 'SUCCESS'
    CREATED = 'created', 'CREATED'
    FAILED = 'failed', 'FAILED'


class ChapaTransactionMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    amount = models.FloatField()
    currency = models.CharField(max_length=25, default='ETB')
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()

    event = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=50, choices=ChapaStatus.choices, default=ChapaStatus.CREATED)

    response_dump = models.JSONField(default=dict)  # incase the response is valuable in the future

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

# TODO: add non abstract model


class ChapaTransaction(ChapaTransactionMixin):
    pass
