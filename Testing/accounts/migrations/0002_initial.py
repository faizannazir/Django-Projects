from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True),
        ),
    ]
