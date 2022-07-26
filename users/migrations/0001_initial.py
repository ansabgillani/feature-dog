# Generated by Django 3.2.14 on 2022-07-27 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('website_link', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('no_of_employees', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professional_email', models.EmailField(max_length=254, unique=True)),
                ('designation', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('MODERATOR', 'Moderator')], default='ADMIN', max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssociatedOrganizationToCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customerprofile')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organizationprofile')),
            ],
        ),
    ]
