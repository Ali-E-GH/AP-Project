from django.db import migrations

def set_defaults(apps, schema_editor):
    QuizResults = apps.get_model('Quizzes', 'QuizResults')
    QuizResults.objects.filter(age_group__isnull=True).update(
        age_group='20_30',
        lifestyle='minimal',
        budget='medium'
    )

class Migration(migrations.Migration):
    dependencies = [
        ('Quizzes', '0004_remove_quizresults_budget_range_max_and_more'),
    ]

    operations = [
        migrations.RunPython(set_defaults),
    ]