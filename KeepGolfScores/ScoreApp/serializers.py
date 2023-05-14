from rest_framework import serializers
from ScoreApp.models import Courses, Scores

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('CourseId', 'CourseName')

class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model=Scores
        fields=('ScoresId', 'Date','Hole1', 'Hole2', 'Hole3', 'Hole4', 'Hole5', 'Hole6' 'Hole7', 'Hole8', 'Hole9', 'Hole10', 'Hole11', 'Hole12', 'Hole13', 'Hole14', 'Hole15', 'Hole17', 'Hole18')