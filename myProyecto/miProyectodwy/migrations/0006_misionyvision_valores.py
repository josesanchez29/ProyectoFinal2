# Generated by Django 2.2.16 on 2020-10-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miProyectodwy', '0005_remove_misionyvision_valores'),
    ]

    operations = [
        migrations.AddField(
            model_name='misionyvision',
            name='valores',
            field=models.TextField(default=1),
        ),
    ]
