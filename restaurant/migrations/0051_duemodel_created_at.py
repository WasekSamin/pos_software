# Generated by Django 3.2 on 2021-12-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0050_duemodel_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='duemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
