from django.db import models


class ChapaTransaction(models.Model):
    first_name = models.CharField(max_length=100)