# Generated by Django 4.1.4 on 2023-03-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_image', models.ImageField(height_field='300', upload_to='', verbose_name='Image', width_field='250')),
                ('db_image', models.BinaryField(verbose_name='Image_db')),
            ],
        ),
    ]