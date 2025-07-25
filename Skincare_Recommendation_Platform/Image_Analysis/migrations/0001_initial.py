# Generated by Django 5.2.1 on 2025-07-03 16:51

import django.contrib.postgres.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageAnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_path', models.ImageField(upload_to='media/')),
                ('detected_issues', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('acne', 'Acne'), ('redness', 'Redness'), ('dark-spots', 'Dark Spots'), ('aging', 'Aging'), ('dullness', 'Dullness')], max_length=30), blank=True, default=list, size=None)),
                ('confidence_scores', models.JSONField(default=list)),
                ('analyzed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
