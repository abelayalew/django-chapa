from django.http.response import JsonResponse
import json


def chapa_webhook(request):
    data = json.loads(request.data)
    return JsonResponse(data)