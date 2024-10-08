# Generated by Django 5.1.1 on 2024-09-16 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
        ('genres', '0001_initial'),
        ('readers', '0001_initial'),
        ('typographies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('year', models.IntegerField(verbose_name='year')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
                ('globalenre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genres.genre')),
                ('reader', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='readers.reader')),
                ('typography', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typographies.typography')),
            ],
        ),
    ]
