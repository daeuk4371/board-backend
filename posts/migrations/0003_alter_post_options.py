# Generated by Django 4.0.5 on 2022-09-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '게시물', 'verbose_name_plural': 'Posts'},
        ),
    ]
