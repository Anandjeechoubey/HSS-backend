# Generated by Django 3.2.4 on 2021-06-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hssapis', '0012_alter_past_talk_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='past_talk',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
