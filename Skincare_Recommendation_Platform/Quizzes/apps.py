from django.apps import AppConfig


class QuizzesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Quizzes'
    def ready(self):
        import Quizzes.signals  # سیگنال‌ها را ایمپورت کنید