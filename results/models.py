from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from exams.models import Exam

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    exam_code = models.CharField(max_length=20, unique=True)
    score = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

