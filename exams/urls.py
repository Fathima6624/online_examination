from django.urls import path

from .views import exam_list,start_exam,subject_list

urlpatterns = [

     path('subjects/', subject_list, name='subject_list'),
      path('exams/<int:subject_id>/',exam_list, name='exam_list'),
     path('start/<int:exam_id>/',start_exam, name='start_exam'),
     

]