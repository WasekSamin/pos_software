# Generated by Django 3.2 on 2021-12-04 10:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255)),
                ('package_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('duration', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('shop_logo', models.ImageField(null=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PackageCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone_number', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAAS.package')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]