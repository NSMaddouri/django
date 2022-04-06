from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from citoyen.models import Citoyen
from citoyen.serializers import CitoyenSerializer

from django.core.files.storage import default_storage


# Create your views here.
@csrf_exempt
def citoyenApi(request, id=0):
    if request.method == 'GET':
        citoyen = Citoyen.objects.get(infoId=id)
        citoyen_serializer = CitoyenSerializer(citoyen)
        return JsonResponse(citoyen_serializer.data, safe=False)

    elif request.method == 'POST':
        citoyen_data = JSONParser().parse(request)
        citoyen_serializer = CitoyenSerializer(data=citoyen_data)
        if citoyen_serializer.is_valid():
            citoyen_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'DELETE':
        citoyen = Citoyen.objects.get(infoId=id)
        citoyen.delete()
        return JsonResponse("Deleted Successfully", safe=False)
