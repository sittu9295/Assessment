from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    title = models.CharField(max_length=255)
    assessment_type = models.CharField(max_length=50, choices=[('quiz', 'Quiz'), ('assignment', 'Assignment'), ('survey', 'Survey')])
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    instructions = models.TextField()
    time_limit = models.IntegerField(null=True, blank=True)
    attempts_allowed = models.IntegerField(default=1)
    is_published = models.BooleanField(default=False)

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[('mcq', 'Multiple Choice'), ('short', 'Short Answer'), ('essay', 'Essay'), ('true_false', 'True/False')])
    answer = models.TextField()

class StudentSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    feedback = models.TextField(null=True)
