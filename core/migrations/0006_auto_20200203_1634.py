# Generated by Django 3.0.2 on 2020-02-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200203_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='baf',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='plot',
            name='alive_trees',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plot',
            name='bd_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='plot',
            name='dead_pine',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='plot',
            name='gross_volume_ha',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='plot',
            name='net_volume_ha',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='plot',
            name='slope',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AddField(
            model_name='plot',
            name='timber_type',
            field=models.CharField(choices=[('Pi/Sx', 'Pi/Sx'), ('Sx/Pi', 'Sx/Pi'), ('Sx/Bl', 'Sx/Bl')], default='Pi/Sx', max_length=100),
        ),
    ]
