from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def chapa_webhook(request):
    if request.method != 'POST':
        return JsonResponse({
            'errors': 'only POST method allowed'
        }, status=400)
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                'error': "Invalid Json Body"
            },
            status=400
        )
    
    model = settings.CHAPA_TRANSACTION_MODEL
    # modify the model instance based on the webhook value
    return JsonResponse(data)
