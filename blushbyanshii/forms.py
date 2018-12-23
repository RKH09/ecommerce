from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from shopping_cart.models import Delivery


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
    username = forms.CharField(widget=forms.TextInput(
                                        attrs={
                                            "class":"input100",
                                            "placeholder":"username"
                                        }
                                        )
                                )
    password = forms.CharField(widget=forms.PasswordInput( attrs={
                                            "class":"input100",
                                            "placeholder":"password"
                                        }))



class SignUpForm(UserCreationForm):
  #  first_name = forms.CharField(max_length=30, widget=forms.TextInput(
   #     attrs={'style': 'border-color:;', 'class': "text", }
   # ), required=False, )
   #last_name = forms.CharField(max_length=30, required=False,)
    username = forms.CharField(max_length=50, widget=forms.TextInput(
         attrs={ 'class': "form-input", 
                 'id'   : "name",
                 'placeholder': "Your Username",
            }
    ), required=True, )
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
         attrs={ 'class': "form-input",
                 'id'   : "email",
                 'placeholder': "Your Email",
        }
    ), required=True, )
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
         attrs={ 'class': "form-input",
                'id'   : "password",
                'placeholder': "Password",
          }
    ), required=True, )
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
         attrs={ 'class': "form-input", 
                'id'   : "re_password",
                'placeholder': "Repeat your password",
         }
    ), required=True, )

    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = ('username','email', 'password1', 'password2', )

#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

class DeliveryForm(forms.Form):
    first_name  =    forms.CharField(max_length=50)
    last_name   =    forms.CharField(max_length=50)
    email       =    forms.EmailField(max_length=150)
    country     =    forms.CharField(max_length=50)
    address     =    forms.CharField(max_length=250)
    town        =    forms.CharField(max_length=150)
    zipcode     =    forms.CharField()
    phone       =    forms.CharField()
    comment     =    forms.CharField()
    delivery    =    forms.BooleanField() 

   