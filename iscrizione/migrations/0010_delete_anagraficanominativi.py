# Generated by Django 3.0.4 on 2020-04-06 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizione', '0009_remove_anagraficanominativi_id_nominativo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnagraficaNominativi',
        ),
    ]