# Generated by Django 5.0.1 on 2024-01-12 15:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto4', '0002_alter_framework_imgframework'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
