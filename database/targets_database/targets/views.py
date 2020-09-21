from targets.models import Target, TargetGroup
from targets.serializers import TargetSerializer, TargetGroupSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


class TargetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        targets = Target.objects.all()
        serializer = TargetSerializer(targets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TargetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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

@csrf_exempt
def targetgroup_list(request):
    if request.method == 'GET':
        targetgroups = TargetGroup.objects.all()
        serializer = TargetGroupSerializer(targetgroups, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TargetGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)