# Generated by Django 4.0.3 on 2022-03-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_expense_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='due_date',
            field=models.DateField(auto_now=True),
        ),
    ]
