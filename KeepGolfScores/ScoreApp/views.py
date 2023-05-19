from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ScoreApp.models import Courses, Scores
from ScoreApp.serializers import CourseSerializers, ScoreSerializers

# Create your views here.

@csrf_exempt
def courseApi(request,id=0):
    if request.method=='GET':
        courses = Courses.objects.all()
        courses_serializer = CourseSerializers(courses, many=True)
        return JsonResponse(courses_serializer.data, safe=False)
    elif request.method=='POST':
        course_data=JSONParser().parse(request)
        courses_serializer=CourseSerializers(data=course_data)
        