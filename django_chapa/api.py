import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from . import models


try:
    SECRET = settings.CHAPA_SECRET
    API_URL = settings.CHAPA_API_URL
    API_VERSION = settings.CHAPA_API_VERSION
    CALLBACK_URL = settings.CHAPA_WEBHOOK_URL
except AttributeError:
    raise ImproperlyConfigured("One or more chapa config missing, please check in your settings file")


class ChapaAPI:
    @classmethod
    def get_headers(cls):
        return {
            'Content-type': 'application/json'
        }

    @classmethod
    def get_url(cls):
        return API_URL + '/' + API_VERSION

    @classmethod
    def send_request(cls, transaction: models.ChapaTransactionMixin):
        data = {
            'amount': transaction.amount,
            'currency': transaction.currency,
            'email': transaction.email,
            'first_name': transaction.first_name,
            'last_name': transaction.last_name,
            'tx_ref': transaction.id,
            'callback_url': CALLBACK_URL,
            'description': transaction.description
        }

        response = requests.post(cls.get_url(), json=data, headers=cls.get_headers())

        return response.json()
