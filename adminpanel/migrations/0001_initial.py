# Generated by Django 3.2 on 2021-12-08 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SAAS', '0016_packagecheckout_is_expired'),
        ('restaurant', '0045_vendor_trade_license'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField(null=True)),
                ('address2', models.TextField(null=True)),
                ('state', models.CharField(max_length=120, null=True)),
                ('zip', models.CharField(max_length=120, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.countrymodel')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop')),
            ],
        ),
    ]
