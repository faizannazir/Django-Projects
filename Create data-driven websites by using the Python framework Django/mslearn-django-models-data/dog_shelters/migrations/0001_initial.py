# Generated by Django 3.1.6 on 2021-02-05 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('adoption_date', models.DateTimeField(null=True)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dog_shelters.shelter')),
            ],
        ),
    ]
