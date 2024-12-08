# Generated by Django 5.1.4 on 2024-12-07 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='branch',
            field=models.ForeignKey(default=str, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='webapp.branch'),
            preserve_default=False,
        ),
    ]