# Generated by Django 4.2.6 on 2023-11-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_colorvarient_discounted_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorvarient',
            name='discount',
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='category_offer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='colorvarient',
            name='product_offer',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
