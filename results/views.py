from django.shortcuts import render
from .models import Result


# Create your views here.
def exam_result(request):
    result = Result.objects.filter(user=request.user).last()
    return render(request, 'result.html', {'result': result})


def search_result(request):
    code = request.GET.get('code')
    result = Result.objects.filter(exam_code=code).first()
    return render(request, 'result.html', {'result': result})
