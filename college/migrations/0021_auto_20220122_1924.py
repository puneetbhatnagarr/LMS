# Generated by Django 3.2.9 on 2022-01-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0020_student_ssem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='brid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='student',
            name='coid',
        ),
        migrations.AlterField(
            model_name='student',
            name='sdesc',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='ssem',
            field=models.CharField(max_length=5),
        ),
    ]
