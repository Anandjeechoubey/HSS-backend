# Generated by Django 3.2.4 on 2021-06-24 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hssapis', '0003_auto_20210624_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeeperson',
            name='committee',
            field=models.CharField(blank=True, choices=[('Departmental Professorial Committee (DPC)', 'Departmental Professorial Committee (DPC)'), ('Departmental Administrative Committee (DAC)', 'Departmental Administrative Committee (DAC)'), ('Department Faculty Assessment Committee (DFAC)', 'Department Faculty Assessment Committee (DFAC)'), ('Departmental Faculty Search Committee (DFSC)', 'Departmental Faculty Search Committee (DFSC)'), ('Safety Committee', 'Safety Committee'), ('Department Web Management Committee (DWMC)', 'Department Web Management Committee (DWMC)'), ('Department Space Management Committee (DSMC)', 'Department Space Management Committee (DSMC)'), ('Department Research Committee (DRC)', 'Department Research Committee (DRC)'), ('Department Academic Programme Committee (DAPC)', 'Department Academic Programme Committee (DAPC)')], max_length=100, null=True),
        ),
    ]