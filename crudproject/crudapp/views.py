from django.shortcuts import render
from .constants import *
import json
from .methods import *
from .models import *
import string
import random
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request, JsonResponse, HttpResponseRedirect
# Create your views here.


@csrf_exempt
def show(request):
    print("****************** loginRender ******************")

    taskDetails = Task.objects.all().values().order_by('-id')
    print("taskDetails ----->",taskDetails)

    return render(request, "show.html", {'baseUrl': baseUrl, 'taskDetails':taskDetails})



@csrf_exempt
def addTask(request):
    print("****************** addTask() ******************")
    response = {}
    if request.method == 'POST':
        try:
            jsonData = request.POST.get('payload')
            parsedData = json.loads(jsonData)
            print("parsedData ---->",parsedData)

            titleName = parsedData.get('titleName')
            print("titleName ----->",titleName)

            description = parsedData.get('description')
            print("description ----->",description)

            status = parsedData.get('status')
            print("status ----->",status)

            Task.objects.create(title=titleName, description=description, status=status).save()

          
            response["status"]=True
            response["message"]= "Task added successfully!"
            return JsonResponse(response)

        except Exception as e :
            print("error ----->",str(e))
            response["status"]=False
            response["message"]= "Something went wrong"
            return JsonResponse(response)
        

@csrf_exempt
def updateTask(request):
    print("****************** updateTask() ******************")
    response = {}
    if request.method == 'POST':
        try:
            jsonData = request.POST.get('payload')
            parsedData = json.loads(jsonData)
            print("parsedData ---->",parsedData)

            taskId = parsedData.get('taskId')
            print("taskId ----->",taskId)

            titleName = parsedData.get('titleName')
            print("titleName ----->",titleName)

            description = parsedData.get('description')
            print("description ----->",description)

            status = parsedData.get('status')
            print("status ----->",status)


            Task.objects.filter(id=taskId).update(title=titleName, description=description, status=status)

          
            response["status"]=True
            response["message"]= "Task updated successfully!"
            return JsonResponse(response)

        except Exception as e :
            print("error ----->",str(e))
            response["status"]=False
            response["message"]= "Something went wrong"
            return JsonResponse(response)
        
@csrf_exempt
def deleteTask(request):
    print("****************** deleteTask() ******************")
    response = {}
    if request.method == 'POST':
        try:
            jsonData = request.POST.get('payload')
            parsedData = json.loads(jsonData)
            print("parsedData ---->",parsedData)

            taskId = parsedData.get('id')
            print("taskId ----->",taskId)

            Task.objects.filter(id=taskId).delete()

            response["status"]=True
            response["message"]= "Task deleted successfully!"
            return JsonResponse(response)

        except Exception as e :
            print("error ----->",str(e))
            response["status"]=False
            response["message"]= "Something went wrong"
            return JsonResponse(response)




@csrf_exempt
def showModalDetails(request):
    print("****************** loginRender ******************")
    response = {}
    if request.method == 'POST':
        try:
            jsonData = request.POST.get('payload')
            parsedData = json.loads(jsonData)
            print("parsedData ---->",parsedData)

            id = parsedData.get('id')
            print("id ----->",id)

            taskDetails = Task.objects.filter(id=id).values()
            print("taskDetails ----->",taskDetails)

            response["status"]=True
            response["message"]= "Success"
            response["taskDetails"]= list(taskDetails)
            return JsonResponse(response)

        except Exception as e :
            print("error ----->",str(e))
            response["status"]=False
            response["message"]= "Something went wrong"
            return JsonResponse(response)

