# Generated by Django 4.2.6 on 2023-10-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_colorvarient_productimage_remove_product_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(default=0),
        ),
    ]
