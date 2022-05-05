# Generated by Django 4.0.2 on 2022-03-01 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagerabbit_app', '0003_theater_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='dates',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='production',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='production',
            name='venue',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]