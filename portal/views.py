from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ClassForm, SubjectForm, ChapterForm, NoteForm, ProfileChangeForm
from .models import Class, Subject, Chapter, Note
from django.contrib import messages


# Create your views here.
@login_required
def dashboard(request):
    return render(request,'portal/dashboard.html')    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

class PasswordChange(SuccessMessageMixin,PasswordChangeView):
    template_name='portal/passwordchange.html'
    success_url='/dashboard/'
    success_message= 'Password Changed Successfully'





def classform(request):
    if request.method == 'POST':
        fm = ClassForm(request.POST)
        if fm.is_valid():
            cn=fm.cleaned_data['class_name']
            ds=fm.cleaned_data['description']
            
            reg=Class(class_name=cn,description=ds)
            fm.save()
            fm = ClassForm()
            messages.success(request,'New Class Added Successfully')    
    else:
        fm = ClassForm()    
    classes= Class.objects.all()
    return render(request, 'portal/class.html', {'form':fm,'classes':classes})


def delete_data(request,id):
    if request.method == "POST":
        pi= Class.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/class/')

def update_data(request, id):
    if request.method == "POST":
        pi = Class.objects.get(pk=id)
        fm = ClassForm(request.POST, instance=pi)
        if fm.is_valid():
            nm=fm.cleaned_data['class_name']
            em=fm.cleaned_data['description']
            reg=Class(class_name=nm,description=em)
            fm.save()
            return HttpResponseRedirect('/class/')
    else:
        pi = Class.objects.get(pk=id)
        fm = ClassForm(instance=pi)    
    return render(request, 'portal/updateclass.html', {'form':fm})            


def subjectform(request):
    if request.method == 'POST':
        fm = SubjectForm(request.POST)
        if fm.is_valid():
            cn=fm.cleaned_data['class_name']
            sn=fm.cleaned_data['subject_name']
            ds=fm.cleaned_data['description']
            
            reg=Subject(class_name=cn,subject_name=sn,description=ds)
            fm.save()
            fm = SubjectForm()
            messages.success(request,'New Subject Added Successfully')    
    else:
        fm = SubjectForm()    
    subject= Subject.objects.all()
    return render(request, 'portal/subject.html', {'form':fm,'subject':subject})

def update_subject(request, id):
    if request.method == "POST":
        pi = Subject.objects.get(pk=id)
        fm = SubjectForm(request.POST, instance=pi)
        if fm.is_valid():
            nm=fm.cleaned_data['class_name']
            sn=fm.cleaned_data['subject_name']
            em=fm.cleaned_data['description']
            reg=Subject(class_name=nm,subject_name=sn,description=em)
            fm.save()
            return HttpResponseRedirect('/subject/')
    else:
        pi = Subject.objects.get(pk=id)
        fm = SubjectForm(instance=pi)    
    return render(request, 'portal/updatesubject.html', {'form':fm})  


    
def delete_subject(request,id):
    if request.method == "POST":
        pi= Subject.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/subject/')


def chapterform(request):
    if request.method == 'POST':
        fm = ChapterForm(request.POST)
        if fm.is_valid():
            cn=fm.cleaned_data['class_name']
            sn=fm.cleaned_data['subject_name']
            ch=fm.cleaned_data['chapter_name']
            ds=fm.cleaned_data['description']
            
            reg=Chapter(class_name=cn,subject_name=sn,chapter_name=ch,description=ds)
            fm.save()
            fm = ChapterForm()
            messages.success(request,'New Chapter Added Successfully')    
    else:
        fm = ChapterForm()    
    chapter= Chapter.objects.all()
    return render(request, 'portal/chapter.html', {'form':fm,'chapter':chapter})

def update_chapter(request, id):
    if request.method == "POST":
        pi = Chapter.objects.get(pk=id)
        fm = ChapterForm(request.POST, instance=pi)
        if fm.is_valid():
            nm=fm.cleaned_data['class_name']
            sn=fm.cleaned_data['subject_name']
            ch=fm.cleaned_data['chapter_name']
            em=fm.cleaned_data['description']
            reg=Chapter(class_name=nm,subject_name=sn,chapter_name=ch,description=em)
            fm.save()
            return HttpResponseRedirect('/chapter/')
    else:
        pi = Chapter.objects.get(pk=id)
        fm = ChapterForm(instance=pi)    
    return render(request, 'portal/updatechapter.html', {'form':fm})  
   
def delete_chapter(request,id):
    if request.method == "POST":
        pi= Chapter.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/chapter/')      



def noteform(request):
    if request.method == 'POST':
        fm = NoteForm(request.POST)
        if fm.is_valid():
            ch=fm.cleaned_data['chapter_name']
            ds=fm.cleaned_data['description']
            url=fm.cleaned_data['url']
            upload=fm.cleaned_data['upload']
            
            reg=Note(chapter_name=ch,description=ds,url=url,upload=upload)
            fm.save()
            fm = NoteForm()
            messages.success(request,'New Note Added Successfully')    
    else:
        fm = NoteForm()    
    note= Note.objects.all()
    return render(request, 'portal/note.html', {'form':fm,'note':note})

def update_note(request, id):
    if request.method == "POST":
        pi = Note.objects.get(pk=id)
        fm = NoteForm(request.POST, instance=pi)
        if fm.is_valid():
            ch=fm.cleaned_data['chapter_name']
            ds=fm.cleaned_data['description']
            url=fm.cleaned_data['url']
            upload=fm.cleaned_data['upload']            
            reg=Note(chapter_name=ch,description=ds,url=url,upload=upload)
            fm.save()
            return HttpResponseRedirect('/note/')
    else:
        pi = Note.objects.get(pk=id)
        fm = NoteForm(instance=pi)    
    return render(request, 'portal/updatenote.html', {'form':fm})  
   
def delete_note(request,id):
    if request.method == "POST":
        pi= Note.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/note/')                  


def profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=ProfileChangeForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Updated Successfully')
                fm.save()                
        else:
            fm=ProfileChangeForm(instance=request.user)
        return render(request,'portal/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')        

      
