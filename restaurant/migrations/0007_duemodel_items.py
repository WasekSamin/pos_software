# Generated by Django 3.2 on 2021-12-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20211201_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='duemodel',
            name='items',
            field=models.ManyToManyField(null=True, to='restaurant.CartItems'),
        ),
    ]