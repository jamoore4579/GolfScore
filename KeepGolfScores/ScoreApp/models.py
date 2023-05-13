from django.db import models

# Create your models here.

class Courses(models.Model):
    Course_List = [
        ('noble hawk', 'Noble Hawk'),
        ('eel river', 'Eel River'),
        ('brookwood', 'Brookwood')
    ]
    
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=20, choices=Course_List),

class Scores(models.Model):
    ScoresId = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now_add=True)
    Hole1 = models.CharField(max_length=2)
    Hole2 = models.CharField(max_length=2)
    Hole3 = models.CharField(max_length=2)
    Hole4 = models.CharField(max_length=2)
    Hole5 = models.CharField(max_length=2)
    Hole6 = models.CharField(max_length=2)
    Hole7 = models.CharField(max_length=2)
    Hole8 = models.CharField(max_length=2)
    Hole9 = models.CharField(max_length=2)
    Hole10 = models.CharField(max_length=2)
    Hole11 = models.CharField(max_length=2)
    Hole12 = models.CharField(max_length=2)
    Hole13 = models.CharField(max_length=2)
    Hole14 = models.CharField(max_length=2)
    Hole14 = models.CharField(max_length=2)
    Hole15 = models.CharField(max_length=2)
    Hole17 = models.CharField(max_length=2)
    Hole18 = models.CharField(max_length=2)