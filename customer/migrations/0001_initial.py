# Generated by Django 3.1.7 on 2021-03-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('adress', models.TextField()),
                ('birthday', models.TextField()),
                ('gender', models.TextField()),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
    ]
