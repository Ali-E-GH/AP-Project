from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, QuizResults

class QuizTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.question = Question.objects.create(
            question="Test Question",
            type="multiple_choice",
            options=["option1", "option2"]
        )

    def test_quiz_submission(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/quiz/', {
            'skin_type': 'oily',
            'concerns': ['acne'],
            'preferences': ['vegan'],
            'budget_min': '10.00',
            'budget_max': '50.00'
        })
        self.assertEqual(response.status_code, 302)  # بررسی ریدایرکت
        self.assertTrue(QuizResults.objects.exists())  # بررسی ذخیره‌سازی داده‌ها