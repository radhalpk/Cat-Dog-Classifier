# Generated by Django 5.0.1 on 2024-01-31 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_usermodel_uloadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='UloadImage',
            field=models.ImageField(upload_to='media/'),
        ),
    ]