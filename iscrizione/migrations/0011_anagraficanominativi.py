# Generated by Django 3.0.4 on 2020-04-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizione', '0010_delete_anagraficanominativi'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnagraficaNominativi',
            fields=[
                ('id_nominativo', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('luogo_di_nascita', models.CharField(blank=True, max_length=50)),
                ('data_nascita', models.DateField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=40)),
            ],
            options={
                'verbose_name': 'Nominativo',
                'verbose_name_plural': 'Nominativi',
            },
        ),
    ]
