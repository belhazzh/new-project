# Generated by Django 4.0.2 on 2022-02-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_medicament_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
