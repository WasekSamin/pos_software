# Generated by Django 3.2.9 on 2021-12-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAAS', '0010_alter_packagecheckout_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
