
# Create your models here.
"""
مدل‌های مربوط به کاربران، نقش‌ها و پروفایل
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.core.models import BaseModel


class CustomUser(AbstractUser):
    """
    مدل کاربر سفارشی با افزودن نقش (Role) و فیلدهای اضافی
    از AbstractUser ارث‌بری می‌کند تا تمام قابلیت‌های پیش‌فرض Django را داشته باشد
    """
    
    class Role(models.TextChoices):
        """
        نقش‌های مختلف کاربران در سیستم
        از TextChoices برای خوانایی بهتر در دیتابیس و admin استفاده شده
        """
        ADMIN = 'ADMIN', 'مدیر سیستم'
        COACH = 'COACH', 'مربی'
        CLIENT = 'CLIENT', 'ورزشکار'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CLIENT,
        verbose_name='نقش کاربری'
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='شماره تلفن'
    )
    profile_picture = models.ImageField(
        upload_to='profiles/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='تصویر پروفایل'
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"

    @property
    def is_coach(self):
        """برای چک کردن راحت‌تر نقش در template ها و view ها"""
        return self.role == self.Role.COACH

    @property
    def is_client(self):
        return self.role == self.Role.CLIENT


class ClientProfile(BaseModel):
    """
    پروفایل تکمیلی برای کاربران با نقش CLIENT
    رابطه OneToOne با CustomUser دارد
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='client_profile',
        verbose_name='کاربر'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='تاریخ تولد'
    )
    height_cm = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='قد (سانتی‌متر)'
    )
    weight_kg = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='وزن (کیلوگرم)'
    )
    goal = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='هدف ورزشی',
        help_text='مثال: کاهش وزن، افزایش حجم عضلانی، آمادگی جسمانی'
    )
    assigned_coach = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clients',
        limit_choices_to={'role': CustomUser.Role.COACH},
        verbose_name='مربی تخصیص‌یافته'
    )

    class Meta:
        verbose_name = 'پروفایل ورزشکار'
        verbose_name_plural = 'پروفایل‌های ورزشکاران'

    def __str__(self):
        return f"پروفایل {self.user.get_full_name() or self.user.username}"
