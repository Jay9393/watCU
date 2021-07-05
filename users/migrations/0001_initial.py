# Generated by Django 3.2.5 on 2021-07-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
