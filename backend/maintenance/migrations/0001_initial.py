# Generated by Django 4.2.15 on 2024-08-31 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('schedule_type', models.CharField(choices=[('manual', 'Manual'), ('auto', 'Auto')], default='manual', max_length=10)),
                ('schedule_date', models.DateField(default=django.utils.timezone.now)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenances', to='vehicles.vehicle')),
            ],
        ),
    ]
