# Generated by Django 4.1.1 on 2022-09-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_productinfo_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='color',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
