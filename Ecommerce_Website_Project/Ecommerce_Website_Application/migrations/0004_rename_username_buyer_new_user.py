# Generated by Django 5.1.6 on 2025-02-28 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Website_Application', '0003_remove_buyer_username_buyer_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='username',
            new_name='New_User',
        ),
    ]
