# Generated by Django 2.2.4 on 2019-08-08 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_red_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='red_num',
            new_name='read_num',
        ),
    ]
