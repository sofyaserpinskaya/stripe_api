# Generated by Django 2.2.19 on 2022-11-29 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20221129_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='items', to='item.Order'),
        ),
    ]