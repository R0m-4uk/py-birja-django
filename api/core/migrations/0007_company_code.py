# Generated by Django 4.2.10 on 2024-02-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_company_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='code',
            field=models.CharField(default=123, max_length=15, verbose_name='Код'),
            preserve_default=False,
        ),
    ]
