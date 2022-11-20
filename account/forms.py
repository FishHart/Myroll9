from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import get_user_model # ユーザーモデルを取得するため
from .models import User


# ユーザーモデル取得
# User = get_user_model()


# class LoginForm(AuthenticationForm):

#     # bootstrap4対応
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class LoginForm(AuthenticationForm):
    pass

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'std_id', 'std_fac', 'std_grd', 'password1', 'password2']

