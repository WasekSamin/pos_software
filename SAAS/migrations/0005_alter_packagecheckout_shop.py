# Generated by Django 3.2 on 2021-12-05 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SAAS', '0004_auto_20211205_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagecheckout',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop'),
        ),
    ]