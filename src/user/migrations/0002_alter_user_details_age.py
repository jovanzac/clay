# Generated by Django 4.1.3 on 2022-11-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
