# Generated by Django 3.0.4 on 2020-04-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizione', '0004_auto_20200402_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventi',
            name='numero_massimo_iscritti',
            field=models.PositiveIntegerField(default=54),
        ),
    ]
