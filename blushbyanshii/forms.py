from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
                                        attrs={
                                            "class":"form-control",
                                            "placeholder":"Full Name"
                                        }
                                        )
                                )
    email = forms.EmailField(widget=forms.TextInput(
                                        attrs={
                                            "class":"form-control",
                                            "placeholder":"Email Address"
                                        }
                                        )
                                )
    Message = forms.CharField(widget=forms.Textarea(
                                        attrs={
                                            "class":"form-control",
                                            "placeholder":"Message"
                                        }
                                        )
                                )

  # def clean_email(self):
       # email = self.cleaned_data.get("email")
      #  if not "gmail.com" in email:
          #  raise forms.ValidationError("Error Found!")
       # return email

class Loginform(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())



class SignUpForm(UserCreationForm):
  #  first_name = forms.CharField(max_length=30, widget=forms.TextInput(
   #     attrs={'style': 'border-color:;', 'class': "text", }
   # ), required=False, )
   # last_name = forms.CharField(max_length=30, required=False,)
  #  email = forms.CharField(max_length=254, )

    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = ('username','password1', 'password2', )

#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
