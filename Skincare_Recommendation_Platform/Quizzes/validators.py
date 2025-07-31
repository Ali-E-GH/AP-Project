from django.core.exceptions import ValidationError

def validate_quiz_data(data):
    if not data.get('skin_type'):
        raise ValidationError("Skin type must be selected.")
    if not data.get('concerns'):
        raise ValidationError("Choose at least one skin concern.")
    # اعتبارسنجی سایر فیلدها...