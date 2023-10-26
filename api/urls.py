from django.urls import path
from . import views


urlpatterns = [
    path('stuinfo/<int:pk>', views.student_detail, name='StuInfo'),
    path('stuinfo/', views.student_list, name='StuList')
]
