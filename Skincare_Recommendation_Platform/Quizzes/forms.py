from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super().__init__(*args, **kwargs)
        
        for question in questions:
            if question.type == 'multiple_choice':
                self.fields[f'q_{question.id}'] = forms.MultipleChoiceField(
                    label=question.question,
                    choices=[(opt, opt) for opt in question.options],
                    widget=forms.CheckboxSelectMultiple,
                    required=False
                )
            elif question.type == 'single_choice':
                self.fields[f'q_{question.id}'] = forms.ChoiceField(
                    label=question.question,
                    choices=[(opt, opt) for opt in question.options],
                    widget=forms.RadioSelect,
                    required=True
                )

    skin_image = forms.ImageField(
        label='uploading image of skin',
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'})
    )

    # فیلدهای اضافی برای دسته‌بندی پاسخ‌ها
    skin_type = forms.CharField(widget=forms.HiddenInput())
    concerns = forms.JSONField(widget=forms.HiddenInput())
    preferences = forms.JSONField(widget=forms.HiddenInput())
    budget = forms.CharField(widget=forms.HiddenInput())
    lifestyle = forms.CharField(widget=forms.HiddenInput())