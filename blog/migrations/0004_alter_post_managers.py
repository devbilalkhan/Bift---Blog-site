# Generated by Django 4.1.5 on 2023-01-22 06:36

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_author_post_author'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
