# Generated by Django 5.0.1 on 2024-02-07 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_company_options_alter_company_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='company_id',
            new_name='company',
        ),
    ]