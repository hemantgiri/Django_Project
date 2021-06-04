from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import Contact, SignupForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# -------------------Login & Sign up----------------------------------------
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required



# Create your views here
def home(request):
    return render(request,'lecture/index.html')


def contact(request):
    fm= Contact()
    name = request.POST.get('name',)
    email = request.POST.get('email',)
    subject = request.POST.get('subject')
    message_data = request.POST.get('message')

    message= f'{name}\n\n{email}\n\n{message_data}'
    if name and subject and message and email:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['hemantgiri1999@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request,'THANK YOU FOR CONTACTING US')
    else:
        fm= Contact()
    return render(request,'lecture/contact.html',{'form':fm}) 


def signup(request):
    if request.method == "POST":
        fm= SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            uname= fm.cleaned_data['username']
            upass= fm.cleaned_data['password2']
            user= authenticate(username=uname,password=upass)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')    
    else:
       fm= SignupForm()
    return render(request,'lecture/signup.html',{'form':fm})  

@login_required
def dashboard(request):
    return render(request,'portal/dashboard.html')
    


    


    