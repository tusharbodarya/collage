from django.urls import path
from main.views import *

urlpatterns = [
    path("department/",DepartmentView.as_view()),
    path("subject/",SubjectView.as_view()),
    path("student-id/",StudentIdView.as_view()),
    path("student/",StudentView.as_view()),
    path("subject-marks/",SubjectMarksView.as_view()),
    path('subject-marks/<int:pk>/students/', SubjectMarksView.students),
]