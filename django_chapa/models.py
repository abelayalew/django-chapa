from django.db import models
from uuid import uuid4


class ChapaTransactionMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    amount = models.FloatField()
    currency = models.CharField(max_length=25, default='ETB')
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        abstract = True
