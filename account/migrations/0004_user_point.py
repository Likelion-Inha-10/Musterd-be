# Generated by Django 4.1 on 2022-08-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(null=True),
        ),
    ]
