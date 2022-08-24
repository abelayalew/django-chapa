from django.urls import path
from . import views

urlpatterns = [
    path('', views.chapa_webhook)
]
