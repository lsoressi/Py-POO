# Generated by Django 5.0.3 on 2024-03-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
