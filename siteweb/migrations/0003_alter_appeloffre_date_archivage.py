# Generated by Django 3.2.3 on 2022-12-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteweb', '0002_auto_20221218_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeloffre',
            name='date_archivage',
            field=models.DateField(),
        ),
    ]
