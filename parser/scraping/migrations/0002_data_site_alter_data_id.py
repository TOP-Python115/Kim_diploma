# Generated by Django 4.1.3 on 2022-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='site',
            field=models.CharField(default='some str', max_length=50),
        ),
        migrations.AlterField(
            model_name='data',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
