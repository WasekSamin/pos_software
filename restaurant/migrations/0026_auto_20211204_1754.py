# Generated by Django 3.2 on 2021-12-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SAAS', '0003_auto_20211204_1713'),
        ('restaurant', '0025_restcheckout_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop'),
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop'),
        ),
    ]