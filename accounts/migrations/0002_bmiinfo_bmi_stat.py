# Generated by Django 2.0.4 on 2018-05-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmiinfo',
            name='bmi_stat',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]