from django.contrib import admin
from .models import Class, Subject, Chapter, Note, Timing, Students
# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=['class_name','description']




@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['class_name','subject_name','description']    
    

@admin.register(Chapter)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['class_name','subject_name','chapter_name']   
    search_fields=['chapter_name']
    


@admin.register(Note)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['chapter_name','description']
    search_fields=['chapter_name']
       

@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display=['date','time']       

@admin.register(Students)
class UserPictureAdmin(admin.ModelAdmin):
    list_display=['user','phone']