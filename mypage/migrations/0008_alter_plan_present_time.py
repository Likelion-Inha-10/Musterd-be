# Generated by Django 4.1 on 2022-08-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0007_plan_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='present_time',
            field=models.IntegerField(),
        ),
    ]
