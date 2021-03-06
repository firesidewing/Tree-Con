# Generated by Django 3.0.2 on 2020-02-07 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200203_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plot',
            name='alive_trees',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='bd_percent',
        ),
        migrations.RemoveField(
            model_name='plot',
            name='dead_pine',
        ),
        migrations.AddField(
            model_name='plotdata',
            name='blowdown',
            field=models.BooleanField(default=0),
        ),
    ]
