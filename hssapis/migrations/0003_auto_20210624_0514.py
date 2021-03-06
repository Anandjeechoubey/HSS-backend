# Generated by Django 3.2.4 on 2021-06-24 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hssapis', '0002_auto_20210624_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='type',
            field=models.CharField(choices=[('Head Of Department', 'Head Of Department'), ('Professor', 'Professor'), ('Assistant Professor', 'Assistant Professor'), ('Associate Professor', 'Associate Professor'), ('Retired Faculty', 'Retired Faculty')], default='Professor', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='Full Time', max_length=20),
        ),
    ]
