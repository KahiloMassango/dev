# Generated by Django 4.1.5 on 2023-01-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='UserName',
            field=models.TextField(blank=True, default=None, max_length=30, null=True),
        ),
    ]