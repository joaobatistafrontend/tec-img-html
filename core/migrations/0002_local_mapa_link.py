# Generated by Django 4.2.7 on 2023-11-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='mapa_link',
            field=models.URLField(default=' '),
        ),
    ]
