# Generated by Django 3.2 on 2021-12-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_duemodel_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duemodel',
            name='items',
            field=models.ManyToManyField(to='restaurant.CartItems'),
        ),
        migrations.AlterField(
            model_name='restcheckout',
            name='items',
            field=models.ManyToManyField(to='restaurant.Item'),
        ),
    ]