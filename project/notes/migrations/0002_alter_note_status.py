# Generated by Django 3.2 on 2022-04-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]