# Generated by Django 2.2.6 on 2019-11-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisapp', '0003_scientist_sci_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scientist',
            old_name='big_stuff',
            new_name='sci_big_stuff',
        ),
    ]