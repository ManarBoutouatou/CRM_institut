# Generated by Django 3.2 on 2022-05-17 18:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='notes',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
