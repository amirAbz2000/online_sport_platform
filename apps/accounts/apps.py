from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = 'مدیریت کاربران'

    def ready(self):
        """
        برای import کردن signals وقتی اپ آماده شد
        در فازهای بعدی از این متد استفاده خواهیم کرد
        """
        pass
