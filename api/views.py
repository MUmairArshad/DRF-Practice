from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerilizer
from rest_framework.renderers import JSONRenderer

# Create your views here.


def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    # print('student object')
    # print(stu)
    serilizer = StudentSerilizer(stu)
    # print('serilizer')
    # print(serilizer)
    # print('Serilizer data')
    # print(serilizer.data)
    # json_data = JSONRenderer().render(serilizer.data)
    # print('Json data')
    # print(json_data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serilizer.data)



def student_list(request):
    stu = Student.objects.all()    
    serilizer = StudentSerilizer(stu, many= True)
    json_data = JSONRenderer().render(serilizer.data)
    
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serilizer.data, safe=False)