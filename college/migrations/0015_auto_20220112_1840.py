# Generated by Django 3.2.9 on 2022-01-12 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_auto_20220112_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_name', models.CharField(max_length=10)),
                ('ass_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='sfile',
        ),
    ]
