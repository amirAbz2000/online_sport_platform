
# Create your models here.
"""
مدل پایه برای همه‌ی مدل‌های دیگر
تمامی مدل‌ها از این کلاس ارث‌بری می‌کنند تا فیلدهای created_at و updated_at را به‌صورت خودکار داشته باشند
"""
from django.db import models


class BaseModel(models.Model):
    """
    مدل انتزاعی پایه با فیلدهای زمان‌سنجی مشترک
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        abstract = True
        # این مدل ذخیره نمی‌شود، فقط برای ارث‌بری است
