# Generated by Django 3.0.2 on 2020-01-27 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200127_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot_number', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plot', to='core.Location')),
                ('userkey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plot', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='plotdata',
            name='plot_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plot_datas', to='core.Plot'),
        ),
        migrations.DeleteModel(
            name='Plots',
        ),
    ]
