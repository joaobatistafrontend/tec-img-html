# Generated by Django 4.2.7 on 2023-11-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_local_mapa_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='mapa_link',
            field=models.URLField(default=' ', max_length=1000),
        ),
    ]
