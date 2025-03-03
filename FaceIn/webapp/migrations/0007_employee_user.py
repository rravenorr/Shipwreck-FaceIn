# Generated by Django 5.1.4 on 2024-12-23 07:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_employee_emp_date_hired_employee_emp_leave_credits'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(default=str, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,  null=True, blank=True),
            preserve_default=False,
        ),
    ]
