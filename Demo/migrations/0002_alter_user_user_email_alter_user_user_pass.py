# Generated by Django 4.1.2 on 2022-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pass',
            field=models.IntegerField(),
        ),
    ]