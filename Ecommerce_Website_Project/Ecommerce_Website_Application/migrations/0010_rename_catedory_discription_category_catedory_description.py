# Generated by Django 5.1.6 on 2025-03-04 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Website_Application', '0009_category_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catedory_discription',
            new_name='catedory_description',
        ),
    ]
