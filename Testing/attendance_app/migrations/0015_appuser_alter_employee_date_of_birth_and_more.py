# Generated by Django 4.1.4 on 2023-07-09 07:51

import attendance_app.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0018_alter_user_email_alter_user_username'),
        ('attendance_app', '0014_employee_db_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('department', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('db_picture', models.BinaryField(blank=True, editable=True, null=True, verbose_name='Image_db')),
                ('date_of_birth', models.DateField(validators=[attendance_app.models.validate_at_least_18_years_old])),
                ('joining_date', models.DateField(validators=[attendance_app.models.validate_not_after_today])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(validators=[attendance_app.models.validate_at_least_18_years_old]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(validators=[attendance_app.models.validate_not_after_today]),
        ),
    ]