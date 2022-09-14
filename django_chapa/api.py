import requests
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from . import models


try:
    SECRET = settings.CHAPA_SECRET
    API_URL = settings.CHAPA_API_URL
    API_VERSION = settings.CHAPA_API_VERSION
    CALLBACK_URL = settings.CHAPA_WEBHOOK_URL
    TRANSACTION_MODEL = settings.CHAPA_TRANSACTION_MODEL
except AttributeError:
    raise ImproperlyConfigured("One or more chapa config missing, please check in your settings file")


class ChapaAPI:
    @classmethod
    def get_headers(cls) -> dict:
        return {
            # 'Content-type': 'application/json',
            'Authorization': f'Bearer {SECRET}'
        }

    @classmethod
    def get_url(cls) -> str:
        return API_URL + '/' + API_VERSION.replace('/', '')

    @classmethod
    def send_request(cls, transaction: models.ChapaTransactionMixin) -> dict:
        data = {
            'amount': transaction.amount,
            'currency': transaction.currency,
            'email': transaction.email,
            'first_name': transaction.first_name,
            'last_name': transaction.last_name,
            'tx_ref': transaction.id.__str__(),
            'callback_url': CALLBACK_URL,
            'description': transaction.description
        }

        response = requests.post(f'{cls.get_url()}/transaction/initialize', json=data, headers=cls.get_headers())

        return response.json()
    
    @classmethod
    def verify_payment(cls, transaction: models.ChapaTransactionMixin) -> dict:
        response = requests.get(
            f'{cls.get_url()}/transaction/verify/{transaction.id}',
            headers=cls.get_headers(),
        )
        return response.json()
