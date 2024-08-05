# Generated by Django 4.2.2 on 2023-07-07 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0002_profile_forget_password_token_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='sem2_sub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='forget_password_token',
            field=models.CharField(default=123, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profie_pic'),
        ),
        migrations.CreateModel(
            name='Sem2_subdet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=100)),
                ('attendance', models.IntegerField(max_length=100)),
                ('sub', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.sem2_sub')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
