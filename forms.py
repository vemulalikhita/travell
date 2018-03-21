from django import forms


from .models import Tour
from .models import Tourist
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout,

)

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = [
            "first_name",
            "content",
            "image",
            ]

class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = [
            "name",
            "content",

            ]

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        #user_qs = User.objects.filter(username=username)
        #if user_qs.count() == 1:
         #   user = user_qs.first()
        if username and password:
            if not user:
                raise forms.ValidationError("This user doesnot exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email adress')
    email2 = forms.EmailField(label='conform Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
     model = User
     fields = [
       'username',
        'email',
        'password',
        ]



     def clean_email(self):
         print(self.cleaned_data)
         email = self.cleaned_email().get('email')
         email2 = self.cleaned_email().get('email2')
         print(email, email2)
         if email != email2:
             raise forms.ValidationError("Emails must match")
         email_qs = User.objects.filter(email=email)
         if email_qs.exists():
            raise forms.ValidationError("This email is already Registered")
         return email