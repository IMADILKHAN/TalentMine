# Generated by Django 3.2.8 on 2022-08-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='no_of_like',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
