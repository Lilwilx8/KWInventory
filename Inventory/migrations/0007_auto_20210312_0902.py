# Generated by Django 3.1.7 on 2021-03-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0006_auto_20210312_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.categoria'),
        ),
    ]
