# Generated by Django 5.0.3 on 2024-04-06 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0005_remove_producto_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Compra.proveedor'),
            preserve_default=False,
        ),
    ]
