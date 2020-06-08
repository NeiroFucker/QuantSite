# Generated by Django 3.0.1 on 2020-05-15 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminsAPI', '0004_auto_20200514_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='autor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
