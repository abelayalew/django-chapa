# Django-Chapa 

Django wrapper for the chapa payment gateway


# Instruction
this package also includes abstract transaction for chapa

## Installation

required python >= 3.6 and django >=3.2 installed

```
pip install django-chapa
```

## Django Config
set your config values in settings.py

```
CHAPA_SECRET = "Secret"

CHAPA_API_URL = ''

CHAPA_API_VERSION = 'v1'

```

add webhook url in urls.py 

```
urlpatterns = [
    path('chapa-webhook', include('django_chapa.urls'))
]
```