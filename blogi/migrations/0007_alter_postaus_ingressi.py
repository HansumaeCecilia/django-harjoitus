# Generated by Django 4.1.7 on 2023-03-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0006_postaus_ingressi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postaus',
            name='ingressi',
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
