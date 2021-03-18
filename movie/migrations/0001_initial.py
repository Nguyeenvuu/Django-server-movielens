# Generated by Django 3.1.7 on 2021-03-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('belongs_to_collection', models.TextField(blank=True, null=True)),
                ('budget', models.IntegerField(blank=True, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('homepage', models.TextField(blank=True, null=True)),
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_language', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('popularity', models.FloatField(blank=True, null=True)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('production_companies', models.TextField(blank=True, null=True)),
                ('release_date', models.TextField(blank=True, null=True)),
                ('revenue', models.BigIntegerField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('tagline', models.TextField(blank=True, null=True)),
                ('vote_average', models.FloatField(blank=True, null=True)),
                ('vote_count', models.IntegerField(blank=True, null=True)),
                ('actor', models.TextField(blank=True, null=True)),
                ('director', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
    ]
