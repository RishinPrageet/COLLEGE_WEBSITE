# Generated by Django 4.2.2 on 2023-07-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_sem2_subdet_classes_present_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem2_subdet',
            name='total_classes',
            field=models.IntegerField(default=100),
        ),
    ]
