from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import QuizResults

@receiver(post_save, sender=QuizResults)
def after_quiz_submission(sender, instance, created, **kwargs):
    if created:
        print(f"Routine creation for user {instance.user} has begun!")  # جایگزین با منطق واقعی