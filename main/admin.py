from django.contrib import admin
from main.models import *

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
    
class StudentIdAdmin(admin.ModelAdmin):
    list_display = ['student_id']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['department','student_id','student_name','student_email','student_age','student_address']
    
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']


admin.site.register(Department,DepartmentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(StudentID,StudentIdAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(SubjectMarks,SubjectMarksAdmin)