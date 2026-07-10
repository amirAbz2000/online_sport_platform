
# Register your models here.
"""
تنظیمات پنل ادمین برای مدل‌های accounts
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, ClientProfile


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """
    سفارشی‌سازی نمایش کاربران در پنل ادمین
    فیلدهای اضافی (role, phone_number) را به فرم‌های پیش‌فرض Django اضافه می‌کند
    """
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']
    
    # افزودن فیلد role به فرم ایجاد و ویرایش کاربر
    fieldsets = BaseUserAdmin.fieldsets + (
        ('اطلاعات اضافی', {'fields': ('role', 'phone_number', 'profile_picture')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('اطلاعات اضافی', {'fields': ('role', 'phone_number')}),
    )


@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    """
    مدیریت پروفایل‌های ورزشکاران در پنل ادمین
    """
    list_display = ['user', 'birth_date', 'height_cm', 'weight_kg', 'assigned_coach']
    list_filter = ['assigned_coach']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']
    raw_id_fields = ['user', 'assigned_coach']  # برای بهبود performance با دیتاست بزرگ
