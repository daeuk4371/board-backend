# Generated by Django 4.0.5 on 2022-09-04 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['created_at'], 'verbose_name': '회원', 'verbose_name_plural': '게시판 회원'},
        ),
    ]