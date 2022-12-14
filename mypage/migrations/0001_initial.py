# Generated by Django 4.1 on 2022-08-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_time', models.DateTimeField(auto_now_add=True)),
                ('isDone', models.BooleanField(default=False)),
                ('promise_time', models.IntegerField()),
                ('title', models.CharField(max_length=30)),
                ('place_name', models.CharField(max_length=30)),
                ('place_id', models.IntegerField()),
                ('max_count', models.IntegerField()),
                ('reward', models.CharField(max_length=30)),
                ('name', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
