# Generated by Django 3.2.9 on 2021-12-07 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SAAS', '0016_packagecheckout_is_expired'),
        ('restaurant', '0035_auto_20211207_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicinePower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_amount', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_cat_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MedicineBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_brand_name', models.CharField(max_length=255)),
                ('med_brand_logo', models.ImageField(upload_to='images/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=255)),
                ('med_image', models.ImageField(upload_to='images/')),
                ('buying_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_out_of_stock', models.BooleanField(default=False)),
                ('stock_amount', models.PositiveIntegerField()),
                ('med_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicinebrand')),
                ('med_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicinecategory')),
                ('med_power', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.medicinepower')),
                ('med_vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.vendor')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
