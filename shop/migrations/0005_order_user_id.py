# Generated by Django 3.1.5 on 2021-01-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
