# Generated by Django 3.2 on 2022-01-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20220125_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='mob',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
