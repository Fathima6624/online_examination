from django.urls import path
from .views import exam_result,search_result

urlpatterns = [
    path('result/', exam_result, name='exam_result'),
     path('result/',search_result, name='search_result'),
]