# Generated by Django 2.2 on 2022-04-23 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartlist',
            old_name='art_id',
            new_name='cart_id',
        ),
    ]
