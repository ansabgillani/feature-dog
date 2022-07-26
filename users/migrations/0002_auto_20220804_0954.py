# Generated by Django 3.2.14 on 2022-08-04 09:54

from django.db import migrations, models
import django.db.models.deletion
import utils.assets


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associatedorganizationtocustomer',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=utils.assets.profile_directory_path),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, upload_to=utils.assets.logo_directory_path),
        ),
        migrations.AlterField(
            model_name='organizationprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=utils.assets.profile_directory_path),
        ),
    ]
