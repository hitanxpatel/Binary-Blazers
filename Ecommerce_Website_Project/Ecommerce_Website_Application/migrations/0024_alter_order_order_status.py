# Generated by Django 5.1.6 on 2025-03-21 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Website_Application', '0023_alter_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order_Placed', 'Ordered Placed'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Out_For_Pickup', 'Out For Pickup'), ('Picked_Up', 'Picked Up'), ('Out_For_Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], default='Order_Placed', max_length=50),
        ),
    ]
