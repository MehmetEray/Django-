# Generated by Django 3.2.5 on 2021-07-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_csv_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesupload',
            name='file',
            field=models.FileField(upload_to='pictures'),
        ),
    ]