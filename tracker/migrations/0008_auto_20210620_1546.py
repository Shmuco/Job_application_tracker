# Generated by Django 3.2.4 on 2021-06-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_joblisting_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='location',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='salary',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
