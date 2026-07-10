"""
فرم‌های مربوط به احراز هویت و پروفایل کاربری
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, ClientProfile


class CustomUserCreationForm(UserCreationForm):
    """
    فرم ثبت‌نام سفارشی با فیلدهای اضافی
    """
    email = forms.EmailField(
        required=True,
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        required=True,
        label='نام',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True,
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        required=False,
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"


class CustomLoginForm(AuthenticationForm):
    """
    فرم ورود سفارشی
    """
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserUpdateForm(forms.ModelForm):
    """
    فرم ویرایش اطلاعات اصلی کاربر
    """
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'profile_picture']


class ClientProfileUpdateForm(forms.ModelForm):
    """
    فرم ویرایش اطلاعات اختصاصی ورزشکار
    """
    class Meta:
        model = ClientProfile
        fields = ['birth_date', 'height_cm', 'weight_kg', 'goal']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
