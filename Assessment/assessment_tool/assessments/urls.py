from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_assessment, name='create_assessment'),
    path('question-bank/', views.manage_question_bank, name='manage_question_bank'),
]
# from django.urls import path
# from .views import CreateAssessmentView

# urlpatterns = [
#     path('create-assessment/', CreateAssessmentView.as_view(), name='create_assessment'),
#     # other URL patterns
# ]
