# Generated by Django 3.2 on 2022-05-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_company_company_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mobile',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
