# Generated by Django 2.2.6 on 2019-11-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisapp', '0002_auto_20191115_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='scientist',
            name='sci_field',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]