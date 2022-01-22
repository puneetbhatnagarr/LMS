# Generated by Django 3.2.7 on 2021-09-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('cemail', models.CharField(default='', max_length=50)),
                ('cmob', models.CharField(max_length=50)),
                ('cadd', models.CharField(max_length=100)),
                ('ccity', models.CharField(max_length=50)),
                ('cweb', models.CharField(max_length=50)),
                ('cdesc', models.CharField(max_length=500)),
                ('cpass', models.CharField(default='12345', max_length=20)),
            ],
        ),
    ]
