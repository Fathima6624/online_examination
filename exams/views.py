

# Create your views here.
from django.shortcuts import render,get_object_or_404, redirect
from .models import Exam, Question,Subject
from django.contrib.auth.decorators import login_required
from results.models import Result




from django.utils import timezone

def exam_list(request, subject_id):
    now = timezone.now()
    exams = Exam.objects.filter(
        subject_id=subject_id,
        start_time__lte=now,
        end_time__gte=now
    )
    return render(request, 'exam_list.html', {'exams': exams})





def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    # Check if already attempted
    if Result.objects.filter(user=request.user, exam=exam).exists():
        return redirect('exam_result')

    questions = Question.objects.filter(exam=exam).order_by('?')[:exam.total_questions]

    if request.method == "POST":
        score = 0
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected == q.correct_answer:
                score += 1

        Result.objects.create(
            user=request.user,
            exam=exam,
            score=score,
            total=exam.total_questions
        )

        return redirect('exam_result')

    return render(request, 'exam_page.html', {
        'exam': exam,
        'questions': questions
    })

  



def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})
