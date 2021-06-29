from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class meta:
        model = CustomUser
        fields = ['username', 'password1','password2','nicknam','user_image','pet']
