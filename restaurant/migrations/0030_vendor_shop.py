# Generated by Django 3.2 on 2021-12-05 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SAAS', '0007_auto_20211205_1732'),
        ('restaurant', '0029_alter_item_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SAAS.shop'),
        ),
    ]