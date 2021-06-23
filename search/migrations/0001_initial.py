# Generated by Django 3.2.4 on 2021-06-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
