# Generated by Django 4.1.2 on 2022-11-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AtmAjax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='card_number',
            field=models.IntegerField(null=True),
        ),
    ]
