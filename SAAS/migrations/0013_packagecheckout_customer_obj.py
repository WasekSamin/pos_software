# Generated by Django 3.2.9 on 2021-12-06 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SAAS', '0012_remove_packagecheckout_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagecheckout',
            name='customer_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
