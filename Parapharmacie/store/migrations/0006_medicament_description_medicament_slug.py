# Generated by Django 4.0.2 on 2022-02-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_subcategorye_remove_medicament_subcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='medicament',
            name='slug',
            field=models.SlugField(default='aa'),
        ),
    ]
