# Generated by Django 3.2.4 on 2024-04-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuki', '0020_auto_20210618_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
