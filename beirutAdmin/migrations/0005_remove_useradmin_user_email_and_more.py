# Generated by Django 5.0.7 on 2024-08-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beirutAdmin', '0004_rename_category_id_menus_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useradmin',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='useradmin',
            name='user_password',
        ),
        migrations.AddField(
            model_name='useradmin',
            name='email',
            field=models.EmailField(db_index=True, default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
