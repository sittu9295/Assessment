from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Assessment, Question

# def dashboard(request):
#     assessments = Assessment.objects.filter(creator=request.user)
#     return render(request, 'assessments/dashboard.html', {'assessments': assessments})

def dashboard(request):
    assessments = Assessment.objects.all()  # Example query; modify as needed
    return render(request, 'assessments/dashboard.html', {'assessments': assessments})


# def dashboard(request):
#     # Assuming 'assessments' is a context variable
#     assessments = []  # Replace with actual data fetching logic
#     return render(request, 'assessments/dashboard.html', {'assessments': assessments})


def create_assessment(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'assessments/create_assessment.html')

def manage_question_bank(request):
    questions = Question.objects.all()
    return render(request, 'assessments/question_bank.html', {'questions': questions})
