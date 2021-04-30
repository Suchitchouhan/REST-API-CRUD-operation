from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.
@api_view(['GET'])
def apioverview(request):
	api_urls = {
	'list':'tasklist'
	}
	return JsonResponse(api_urls)

@api_view(['GET'])
def tasklist(request):
	task=Task.objects.all()
	serializer = TaskSerializer(task,many=True)
	return Response(serializer.data)


@api_view(['GET'])
def taskdetails(request,pk):
	task=Task.objects.get(id=pk)
	serializer = TaskSerializer(task,many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskcreate(request):
	context={}
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		context['status']="Task has been successfully created"

	return Response(context)	


@api_view(['POST'])
def taskupdate(request,pk):
	context={}
	task=Task.objects.get(pk=pk)
	serializer = TaskSerializer(instance=task,data=request.data)
	if serializer.is_valid():
		serializer.save()
		context['status']="Task has been successfully created"
	return Response(context)		