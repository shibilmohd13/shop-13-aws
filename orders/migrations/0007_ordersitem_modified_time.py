# Generated by Django 4.2.6 on 2023-11-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_orders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersitem',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
