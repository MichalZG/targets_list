from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def target_list(request):
    if request.method == 'GET':
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TargetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
def target_detail(request, pk):
    """
    Retrieve, update or delete a code target.
    """
    try:
        target = Target.objects.get(pk=pk)
    except Target.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TargetSerializer(target)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TargetSerializer(target, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        target.delete()
        return HttpResponse(status=204)