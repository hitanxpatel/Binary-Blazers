# Generated by Django 5.1.6 on 2025-03-16 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Website_Application', '0013_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_buyer_first_name', models.CharField(max_length=250)),
                ('order_buyer_last_name', models.CharField(max_length=250)),
                ('order_buyer_email', models.CharField(max_length=250)),
                ('order_buyer_contact', models.CharField(max_length=250)),
                ('order_buyer_address', models.CharField(max_length=250)),
                ('order_seller_name', models.CharField(max_length=250)),
                ('order_seller_email', models.CharField(max_length=250)),
                ('order_seller_contact', models.CharField(max_length=250)),
                ('order_seller_address', models.CharField(max_length=250)),
                ('order_product_name', models.CharField(max_length=250)),
                ('order_product_price', models.CharField(max_length=250)),
                ('order_quantity', models.IntegerField()),
                ('order_total', models.IntegerField()),
                ('order_status', models.CharField(choices=[('Order_Placed', 'Ordered Placed'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Out_For_Pickup', 'Out For Pickup'), ('Picked_Up', 'Picked Up'), ('Out_For_Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], default='Order_Placed', max_length=50)),
                ('order_buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce_Website_Application.buyer')),
                ('order_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce_Website_Application.product')),
                ('order_seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ecommerce_Website_Application.seller')),
            ],
        ),
    ]
