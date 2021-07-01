from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class meta:
        model = CustomUser
        fields = ['username', 'password1','email','pet']
