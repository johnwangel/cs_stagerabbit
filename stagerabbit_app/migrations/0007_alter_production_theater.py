# Generated by Django 4.0.2 on 2022-03-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stagerabbit_app', '0006_alter_production_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theaters', to='stagerabbit_app.theater'),
        ),
    ]
