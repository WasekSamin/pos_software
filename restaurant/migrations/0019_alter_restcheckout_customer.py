# Generated by Django 3.2 on 2021-12-04 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0018_auto_20211202_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restcheckout',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer'),
        ),
    ]
