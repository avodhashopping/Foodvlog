# Generated by Django 2.2 on 2022-05-01 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20220423_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist'),
        ),
    ]
