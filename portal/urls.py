
from django.urls import path
from . import views
from .forms import PasswordChangeForm
from django.contrib import admin

admin.site.site_header = 'Shunya'
admin.site.site_title = 'Shunya'
urlpatterns = [
 
  path('dashboard/',views.dashboard,name='dashboard'),
  path('change_password/',views.PasswordChange.as_view(form_class=PasswordChangeForm),name='passwordchange'),
  path('logout/',views.logout_view,name='logout'),
  path('class/',views.classform,name='class'),
  path('delete/<int:id>/',views.delete_data,name="deletedata"),
  path('update/<int:id>/',views.update_data,name="updatedata"),
  

  path('subject/',views.subjectform,name='subject'),
  path('deletec_sub/<int:id>/',views.delete_subject,name="deletesubject"),
  path('update_sub/<int:id>/',views.update_subject,name="updatesubject"),

  
  path('chapter/',views.chapterform,name='chapter'),
  path('deletec_chap/<int:id>/',views.delete_chapter,name="deletechapter"),
  path('update_chap/<int:id>/',views.update_chapter,name="updatechapter"),


  
  path('note/',views.noteform,name='note'),
  path('deletec_note/<int:id>/',views.delete_note,name="deletenote"),
  path('update_note/<int:id>/',views.update_note,name="updatenote"),


  path('profile/',views.profile,name="profile"),
  
]
