# Generated by Django 4.2.2 on 2023-07-09 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_sem1_sub_sem1_subdet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem1_subdet',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.sem1_sub'),
        ),
    ]
