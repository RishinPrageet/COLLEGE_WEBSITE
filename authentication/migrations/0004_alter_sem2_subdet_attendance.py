# Generated by Django 4.2.2 on 2023-07-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_sem2_sub_alter_profile_forget_password_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem2_subdet',
            name='attendance',
            field=models.IntegerField(),
        ),
    ]
