from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Students(models.Model):
        user = models.OneToOneField(User, on_delete = models.CASCADE)
        address=models.CharField(max_length=300,default='')
        phone=models.IntegerField(default=0)
        picture = models.ImageField(blank=True)
        class Meta:
            verbose_name = 'Student'
            verbose_name_plural = 'Students'


class Class(models.Model):
    class_name= models.CharField(max_length=10)
    description = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
    def __str__(self):
        return self.class_name

class Subject(models.Model):
    class_name= models.ForeignKey(Class,on_delete=models.CASCADE)
    subject_name= models.CharField(max_length=15)
    description= models.CharField(max_length=300)
    def __str__(self):
        return self.subject_name

class Chapter(models.Model):
    class_name=models.ForeignKey(Class,on_delete=models.CASCADE)
    subject_name= models.ForeignKey(Subject,on_delete=models.CASCADE)
    chapter_name=models.CharField(max_length=250)
    description=models.TextField(max_length=500)
    def __str__(self):
        return self.chapter_name

class Note(models.Model):
    chapter_name= models.OneToOneField(Chapter,on_delete=models.CASCADE)
    description= models.TextField(max_length=500)
    url= models.URLField(max_length=300, blank=True, default="")
    upload= models.FileField(upload_to=None)
    def __str__(self):
        return 'Notes'

class Timing(models.Model):
    date= models.DateField()
    time=models.TimeField()
        