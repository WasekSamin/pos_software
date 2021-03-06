# Generated by Django 3.2 on 2021-12-11 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SAAS', '0017_auto_20211211_1145'),
        ('restaurant', '0048_auto_20211211_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.item'),
        ),
        migrations.AlterField(
            model_name='category',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='duemodel',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.customer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.brand'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.vendor'),
        ),
        migrations.AlterField(
            model_name='refundmodel',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.restcheckout'),
        ),
        migrations.AlterField(
            model_name='refundmodel',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='restcheckout',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.customer'),
        ),
        migrations.AlterField(
            model_name='restcheckout',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='table',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='tablecheckout',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SAAS.shop'),
        ),
        migrations.AlterField(
            model_name='tablecheckout',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.table'),
        ),
        migrations.AlterField(
            model_name='tableitems',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.item'),
        ),
    ]
