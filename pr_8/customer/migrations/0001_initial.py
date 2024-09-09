# Generated by Django 5.1 on 2024-09-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('number', models.IntegerField(blank=True, db_index=True, unique=True, verbose_name='Номер телефона')),
                ('email', models.CharField(blank=True, max_length=150, unique=True, verbose_name='E-mail')),
            ],
        ),
    ]
