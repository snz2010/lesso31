# Generated by Django 4.0.5 on 2022-06-16 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_ad_created_alter_ad_name_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='category_id',
            new_name='category',
        ),
    ]
