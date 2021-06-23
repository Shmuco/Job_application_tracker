# Generated by Django 3.2.4 on 2021-06-21 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_auto_20210620_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='joblisting',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.location'),
        ),
    ]
