from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm, UserChangeForm
from .models import Class, Subject, Chapter, Note, Students



class PasswordChangeForm(SetPasswordForm):
 old_password = forms.CharField(label='Old Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 new_password1 = forms.CharField(label='New Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 new_password2 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
    model = User    

class ClassForm(forms.ModelForm):
   class Meta:
      model= Class
      fields=['class_name','description']
      # labels={'class_name':'Class Name','description':'Description'}
      widgets = {
        'class_name':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.TextInput(attrs={'class':'form-control'}),        
        }
      
class SubjectForm(forms.ModelForm):
   class Meta:
      model= Subject
      fields=['class_name','subject_name','description']
      # labels={'class_name':'Class Name','description':'Description'}
      widgets = {
        'class_name':forms.Select(attrs={'class':'form-control'}),
        'subject_name':forms.TextInput(attrs={'class':'form-control'}),        
        'description':forms.TextInput(attrs={'class':'form-control'}),        
        }


class ChapterForm(forms.ModelForm):
   class Meta:
      model= Chapter
      fields=['class_name','subject_name','chapter_name','description']
      # labels={'class_name':'Class Name','description':'Description'}
      widgets = {
        'class_name':forms.Select(attrs={'class':'form-control'}),
        'subject_name':forms.Select(attrs={'class':'form-control'}),        
        'chapter_name':forms.TextInput(attrs={'class':'form-control'}),        
        'description':forms.TextInput(attrs={'class':'form-control'}),        
        }



class NoteForm(forms.ModelForm):
   class Meta:
      model= Note
      fields=['chapter_name','description','url','upload']
      # labels={'class_name':'Class Name','description':'Description'}
      widgets = {
        'chapter_name':forms.Select(attrs={'class':'form-control'}),
        'description':forms.TextInput(attrs={'class':'form-control'}),        
        'url':forms.URLInput(),        
        'upload':forms.FileInput(),        
        }


class ProfileChangeForm(UserChangeForm):
   password=None   
   class Meta:
      model= User
      # widgets={
      #    'last_login':forms.DateTimeInput(attrs={'disabled':'disabled'}),
      #    'date_joined':forms.DateTimeInput(attrs={'disabled':'disabled'})
      # }
      fields= ['first_name','last_name','email']

class ProfileDetail(forms.ModelForm):
      class Meta:
            model = Students
            fields=['address','phone','picture']      




