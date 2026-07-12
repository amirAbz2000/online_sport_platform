# ✅ چک‌لیست فاز ۱: راه‌اندازی اولیه پروژه Django

## 🏗️ ساختار پروژه و محیط

- [x] ایجاد محیط مجازی Python (`venv`)
- [x] نصب Django 5.x و پکیج‌های پایه (`requirements.txt`)
- [x] ساختار ماژولار پروژه (`config/` و `apps/`)
- [x] تنظیم `.env.example` و `.env` برای متغیرهای محیطی
- [x] پیکربندی `.gitignore` برای امنیت کد

## ⚙️ تنظیمات پروژه

- [x] جداسازی settings به `base.py`، `development.py`، `production.py`
- [x] تنظیم `DJANGO_SETTINGS_MODULE` در `manage.py` (development)
- [x] تنظیم `DJANGO_SETTINGS_MODULE` در `wsgi.py` و `asgi.py` (production)
- [x] پیکربندی دیتابیس SQLite برای توسعه
- [x] تنظیم مسیرهای `STATIC_URL`، `MEDIA_URL`، `TEMPLATES`

## 👤 سیستم کاربری (apps/accounts)

- [x] ایجاد مدل `CustomUser` (ارث‌بری از `AbstractUser`)
- [x] تعریف نقش‌های کاربری: ADMIN، COACH، CLIENT
- [x] ایجاد مدل `ClientProfile` برای اطلاعات تکمیلی ورزشکاران
- [x] تنظیم `AUTH_USER_MODEL = 'accounts.CustomUser'`
- [x] پیکربندی پنل ادمین Django برای مدیریت کاربران

## 🔐 سیستم احراز هویت

- [x] فرم و ویوی ثبت‌نام (`RegisterView`)
- [x] فرم و ویوی ورود (`LoginView`)
- [x] ویوی خروج (`LogoutView`)
- [x] مسیرهای بازیابی و تغییر رمز عبور (Password Reset)
- [x] ساخت خودکار `ClientProfile` برای کاربران CLIENT

## 📄 قالب‌ها و رابط کاربری

- [x] قالب پایه `base.html`
- [x] صفحه اصلی `home.html`
- [x] قالب ثبت‌نام `accounts/register.html`
- [x] قالب ورود `accounts/login.html`
- [x] داشبورد کاربری `accounts/dashboard.html`
- [x] صفحه پروفایل `accounts/profile.html`

## 🔧 پیکربندی‌های تکمیلی

- [x] نصب و تنظیم `django-crispy-forms` با Tailwind
- [x] ساختار فولدر `static/` و `media/`
- [x] مدل پایه `BaseModel` با `created_at` و `updated_at`

## 🗄️ دیتابیس

- [x] اجرای `makemigrations` و `migrate`
- [x] ایجاد superuser برای دسترسی به پنل ادمین
- [x] تست ثبت کاربر جدید و ورود به سیستم

## 🧪 تست و اجرا

- [x] اجرای موفق `runserver` بدون خطا
- [x] تست عملکرد فرم‌های ثبت‌نام و ورود
- [x] تست داشبورد و ویرایش پروفایل
- [x] تست پنل ادمین Django

---

## 📋 نتیجه‌گیری

**وضعیت فاز ۱:** ✅ **کامل شده**

**آماده برای فاز ۲:** ✅ پلن‌ها و سیستم پرداخت

---

## 🚀 فازهای بعدی (پیش‌بینی)

### فاز ۲: پلن‌ها و پرداخت
- مدل‌های `Plan`, `Subscription`, `Payment`
- درگاه پرداخت
- مدیریت اشتراک‌ها

### فاز ۳: فرم‌های ارزیابی
- مدل `AssessmentForm`
- فرم‌های پویا
- ذخیره پاسخ‌ها

### فاز ۴: سیستم برنامه تمرینی
- مدل‌های `Exercise`, `WorkoutProgram`
- انتخاب تمرین توسط AI
- تایید مربی

### فاز ۵: تیکتینگ و پشتیبانی
- مدل `Ticket`
- سیستم پیام‌رسانی

### فاز ۶: وبلاگ و محتوا
- مدل `Post`
- مدیریت مقالات

### فاز ۷: PDF و گزارش‌گیری
- WeasyPrint
- تولید PDF برنامه تمرینی

### فاز ۸: دیپلوی و بهینه‌سازی
- آماده‌سازی production
- Redis و Celery
- S3 Storage

---

**تاریخ تکمیل فاز ۱:** 1405/04/20 (2026/07/11)
