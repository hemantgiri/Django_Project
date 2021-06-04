
from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from lecture.forms import LoginForm, SignupForm, Contact, PasswordReset, ResetForm
# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('',views.home,name='home'),
  path('contact/',views.contact,name='contact'),
  path('signup/',views.signup,name='signup'),
 
  # ---------------------LOGIN URLS---------------------------------------------------------------------------------------------
  path('login/',views.LoginView.as_view(template_name='lecture/login.html', authentication_form=LoginForm),name='login'),
  
  
  path('forgotpassword',views.PasswordResetView.as_view(template_name='lecture/forgotpassword.html',success_url='resetpassworddone/',form_class=PasswordReset),name='forgotpassword'),
  path('resetpassworddone/',views.PasswordResetDoneView.as_view(template_name='lecture/resetdone.html'),name='resetdone'),

  path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name="registration/resetconfirm.html",form_class=ResetForm),name='password_reset_confirm'),
  path('reset/done/',views.PasswordResetCompleteView.as_view(template_name="registration/resetcomplete.html"),name='password_reset_complete'),
  
]