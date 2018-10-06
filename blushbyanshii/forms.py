from django import forms

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