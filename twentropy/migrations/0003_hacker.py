# Generated by Django 3.0.2 on 2020-01-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twentropy', '0002_tweet_sensitive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(null=True)),
                ('email', models.CharField(max_length=1000, null=True)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]