from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.serializers import *
from main.models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from rest_framework.decorators import action
from django.http import JsonResponse


class DepartmentView(APIView):
    def get(self, request):
        try:
            department_obj = Department.objects.all()
            if request.GET.get("search"):
                search = request.GET.get("search")
                department_obj = Department.objects.filter(department__icontains=search)
            page_number = request.GET.get("page", 1)
            paginator = Paginator(department_obj, 10)
            dept_serializer = DepartmentSerializer(
                paginator.page(page_number), many=True
            )
            return Response(
                {
                    "status": True,
                    "message": "Department List.",
                    "data": dept_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Something went wrong.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class SubjectView(APIView):
    def get(self, request):
        try:
            subject_obj = Subject.objects.all()
            if request.GET.get("search"):
                search = request.GET.get("search")
                subject_obj = Subject.objects.filter(subject_name__icontains=search)
            page_number = request.GET.get("page", 1)
            paginator = Paginator(subject_obj, 10)
            dept_serializer = SubjectSerializer(paginator.page(page_number), many=True)
            return Response(
                {
                    "status": True,
                    "message": "Subject List.",
                    "data": dept_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False, 
                    "message": "Something went wrong.", 
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class StudentIdView(APIView):
    def get(self, request):
        try:
            student_id_obj = StudentID.objects.all()
            if request.GET.get("search"):
                search = request.GET.get("search")
                student_id_obj = StudentID.objects.filter(student_id__icontains=search)
            page_number = request.GET.get("page", 1)
            paginator = Paginator(student_id_obj, 10)
            dept_serializer = StudentIdSerializer(
                paginator.page(page_number), many=True
            )
            return Response(
                {
                    "status": True,
                    "message": "Student Id List.",
                    "data": dept_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Something went wrong.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class StudentView(APIView):
    def get(self, request):
        try:
            student_obj = Student.objects.all()
            if request.GET.get("search"):
                search = request.GET.get("search")
                student_obj = Student.objects.filter(
                    Q(department__department__icontains=search)
                    | Q(student_id__student_id__icontains=search)
                    | Q(student_name__icontains=search)
                    | Q(student_email__icontains=search)
                    | Q(student_age__icontains=search)
                    | Q(student_address__icontains=search)
                )
            page_number = request.GET.get("page", 1)
            paginator = Paginator(student_obj, 10)
            dept_serializer = StudentSerializer(paginator.page(page_number), many=True)
            return Response(
                {
                    "status": True,
                    "message": "Student List.",
                    "data": dept_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Something went wrong.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class SubjectMarksView(APIView):
    def get(self, request):
        try:
            subject_mark_obj = SubjectMarks.objects.all()
            page_number = request.GET.get("page", 1)
            paginator = Paginator(subject_mark_obj, 10)
            dept_serializer = SubjectMarksSerializer(
                paginator.page(page_number), many=True
            )
            return Response(
                {
                    "status": True,
                    "message": "Subject Mark List.",
                    "data": dept_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": False, 
                    "message": "Something went wrong.", 
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=True, methods=["get"])
    def students(request, pk=None):
        try:
            subject_mark_obj = SubjectMarks.objects.filter(
                student__student_id__student_id=pk
            )
            total_marks = subject_mark_obj.aggregate(total_marks=Sum("marks"))
            dept_serializer = SubjectMarksSerializer(subject_mark_obj, many=True)
            return JsonResponse(
                {
                    "status": True,
                    "message": "Subject Mark List.",
                    "data": dept_serializer.data,
                    "total_marks": total_marks,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return JsonResponse(
                {
                    "status": False,
                    "message": "Something went wrong.",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
