# Generated by Django 4.1.1 on 2022-09-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saicreations_app', '0002_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]