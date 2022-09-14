from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json


@csrf_exempt
def chapa_webhook(request):
    # who knows what kind of request we are getting
    if request.method != 'POST':
        return JsonResponse(
            {
                'errors': 'only POST method allowed'
            },
            status=400,
        )

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
    # add your webhook events here and also you can override the model
    model.response_dump = data
    model.save()
    # TODO: this method should be class view for customization support
    return JsonResponse(data)
