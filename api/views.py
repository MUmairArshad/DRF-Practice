from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serilizer = StudentSerilizer(stu)
    return JsonResponse(serilizer.data)



def student_list(request):
    stu = Student.objects.all()    
    serilizer = StudentSerilizer(stu, many= True)
    json_data = JSONRenderer().render(serilizer.data)
    
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serilizer.data, safe=False)



@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serilizer = StudentSerilizer(data=pythondata)

        if serilizer.is_valid():
            serilizer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'applicaton/json')
        
        json_data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data, content_type = 'applicaton/json')