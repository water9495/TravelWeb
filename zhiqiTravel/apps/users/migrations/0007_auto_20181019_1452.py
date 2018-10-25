# Generated by Django 2.1.2 on 2018-10-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20181018_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='city',
            new_name='city_addr',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(default='', max_length=15, verbose_name='昵称'),
        ),
    ]
