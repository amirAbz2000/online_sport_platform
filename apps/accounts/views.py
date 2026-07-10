

"""
نماهای مربوط به احراز هویت و مدیریت پروفایل
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm, UserUpdateForm, ClientProfileUpdateForm
from .models import ClientProfile


class RegisterView(CreateView):
    """
    نمای ثبت‌نام کاربر جدید
    """
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        # بعد از ثبت‌نام، اگر نقش ورزشکار بود، پروفایل برایش ساخته می‌شود
        user = form.save()
        if user.role == user.Role.CLIENT:
            ClientProfile.objects.get_or_create(user=user)
        messages.success(self.request, 'ثبت‌نام شما با موفقیت انجام شد. اکنون وارد شوید.')
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """
    نمای ورود به سیستم
    """
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'


class LogoutView(View):
    """
    خروج از سیستم
    """
    def get(self, request):
        logout(request)
        messages.info(request, "با موفقیت خارج شدید.")
        return redirect('home')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    پنل کاربری (مبنا بر اساس نقش تغییر می‌کند)
    """
    template_name = 'accounts/dashboard.html'


class ProfileView(LoginRequiredMixin, View):
    """
    ویرایش پروفایل کاربر و اطلاعات ورزشی
    """
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {
            'user_form': UserUpdateForm(instance=user),
        }
        if user.is_client:
            profile, created = ClientProfile.objects.get_or_create(user=user)
            context['profile_form'] = ClientProfileUpdateForm(instance=profile)
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        user = request.user
        user_form = UserUpdateForm(request.POST, request.FILES, instance=user)

        profile_form = None
        if user.is_client:
            profile = ClientProfile.objects.get(user=user)
            profile_form = ClientProfileUpdateForm(request.POST, instance=profile)

        if 'update_user' in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'اطلاعات کاربری با موفقیت بروز شد.')
                return redirect('accounts:profile')

        elif 'update_profile' in request.POST and profile_form:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'اطلاعات ورزشی با موفقیت بروز شد.')
                return redirect('accounts:profile')

        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })
