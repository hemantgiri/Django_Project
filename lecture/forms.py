from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, PasswordResetForm, SetPasswordForm 

class Contact(forms.Form):
    name = forms.CharField(required=True,label='Name', max_length=100,widget=forms.TextInput(attrs={'id':'formGroupExampleInputMD','class':'form-control '}))
    email= forms.CharField(required=True,label='Email',min_length=10,widget=forms.TextInput(attrs={'id':'formGroupExampleInputMD','class':'form-control'}))
    subject= forms.CharField(required=True,label='Subject', max_length=300,widget=forms.TextInput(attrs={'id':'formGroupExampleInputMD','class':'form-control'}))
    message= forms.CharField(required=True,label='Message',widget=forms.Textarea(attrs={'id':'formGroupExampleInputMD','class':'form-control',}))


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control '}))
    password= forms.CharField(
        label= ('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control '}),
    )    
Grade = (
                            ('class_9','Class 9'),
                            ('class_10', 'Class 10'),
                            ('class_11','Class 11'),
                            ('class_12','Class 12'),
                            
                        )



class SignupForm(UserCreationForm):  
    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control '}))
    password2= forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control '}))
    grade= forms.CharField(widget=forms.Select(choices=Grade,attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email','grade']
        labels={'username':'Username','first_name':'First Name','last_name':'Last Name','grade':'Grade'}
        

class PasswordReset(PasswordResetForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        



class ResetForm(SetPasswordForm):
 new_password1 = forms.CharField(label='New Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 new_password2 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
    model = User
    


class PasswordChangeForm(SetPasswordForm):
 old_password = forms.CharField(label='Old Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 new_password1 = forms.CharField(label='New Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 new_password2 = forms.CharField(label='Confirm Password ',widget=forms.PasswordInput(attrs={'class':'form-control'}))
 class Meta:
    model = User    