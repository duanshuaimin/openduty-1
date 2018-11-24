# Generated by Django 2.1.3 on 2018-11-22 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='service_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incident', to='services.Service'),
        ),
        migrations.AddField(
            model_name='incident',
            name='service_to_escalate_to',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_to_escalate_to_id', to='services.Service'),
        ),
        migrations.AlterUniqueTogether(
            name='incident',
            unique_together={('service_key', 'incident_key')},
        ),
    ]