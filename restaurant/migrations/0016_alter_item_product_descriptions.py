# Generated by Django 3.2 on 2021-12-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_item_product_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product_descriptions',
            field=models.TextField(null=True),
        ),
    ]
