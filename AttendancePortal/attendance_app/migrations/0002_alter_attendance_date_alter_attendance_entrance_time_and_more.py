# Generated by Django 4.1.4 on 2023-03-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='entrance_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='exit_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='total_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]