# Generated by Django 2.2.14 on 2021-06-17 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kuki', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
