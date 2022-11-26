# Generated by Django 4.1.3 on 2022-11-25 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_pressure', models.IntegerField()),
                ('heart_rate', models.IntegerField()),
                ('oxygen_level', models.IntegerField()),
                ('body_temp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.IntegerField()),
                ('normal_min', models.IntegerField()),
                ('normal_max', models.IntegerField()),
                ('user_vitals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.uservitals')),
            ],
        ),
    ]
