# Generated by Django 5.0.3 on 2024-04-06 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compra', '0002_rename_dni_proveedor_cuit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=30)),
                ('stock_actual', models.IntegerField(max_length=30)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Compra.proveedor')),
            ],
        ),
    ]
