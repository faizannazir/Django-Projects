# Generated by Django 4.1.4 on 2023-03-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('employee_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile', models.ImageField(upload_to='')),
                ('department', models.CharField(choices=[('IT', 'IT DEPARTMENT'), ('managment', 'MANAGMENT DEPARTMENT'), ('finance', 'FINANCE DEPARTMENT')], max_length=200)),
                ('contact', models.CharField(max_length=13)),
            ],
        ),
    ]
