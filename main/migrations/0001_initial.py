# Generated by Django 4.0.4 on 2022-05-27 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=11)),
                ('kasb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.jobs')),
            ],
        ),
    ]
