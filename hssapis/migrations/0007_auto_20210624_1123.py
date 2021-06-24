# Generated by Django 3.2.4 on 2021-06-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hssapis', '0006_alter_award_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeeperson',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='committee/'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='faculty/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='office_staff',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='staff/'),
        ),
        migrations.AlterField(
            model_name='phd_awarded',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='phd_awarded/'),
        ),
        migrations.AlterField(
            model_name='special_talk',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='special_talk/'),
        ),
        migrations.AlterField(
            model_name='special_talk',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='special_talk/'),
        ),
        migrations.AlterField(
            model_name='special_talk',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='special_talk/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='student/'),
        ),
    ]
