# Generated by Django 5.0.1 on 2024-01-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_usermodel_uloadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='Name',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]