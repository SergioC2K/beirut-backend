# Generated by Django 5.0.7 on 2024-08-10 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beirutAdmin', '0003_categories_alter_reservations_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menus',
            old_name='category_id',
            new_name='category',
        ),
    ]
