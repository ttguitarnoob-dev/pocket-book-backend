# Generated by Django 4.0.3 on 2022-03-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_budget_budget_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='name',
            field=models.CharField(default='New Budget', max_length=100),
        ),
    ]