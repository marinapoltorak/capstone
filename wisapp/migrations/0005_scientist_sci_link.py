# Generated by Django 2.2.6 on 2019-11-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisapp', '0004_auto_20191115_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='sci_link',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]