# Generated by Django 5.0.3 on 2024-07-11 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0002_auto_20240319_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categorias',
        ),
        migrations.AlterField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.producto'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_online.usuario'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='talla',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Despacho',
        ),
    ]
