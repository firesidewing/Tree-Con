# Generated by Django 3.0.2 on 2020-02-03 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200127_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=255)),
                ('loss_factor', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='plotdata',
            name='species',
        ),
        migrations.AddField(
            model_name='plotdata',
            name='tree_species',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tree_species', to='core.Species'),
        ),
    ]
