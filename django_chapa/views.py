from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.apps import apps
import json


@csrf_exempt
def chapa_webhook(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                'error': "Invalid Json Body"
            },
            status=400
        )
    
    model_class = apps.get_model(settings.CHAPA_TRANSACTION_MODEL)
    try:
        transaction_instance = model_class.objects.get(id=data.get('trx_ref'))
        transaction_instance.status = data.get('status')
        transaction_instance.response_dump = data
        transaction_instance.save()
        return JsonResponse(data)
    except model_class.DoesNotExist:
        return JsonResponse(
            {
                'error': "Invalid Transaction"
            },
            status=400
        )
