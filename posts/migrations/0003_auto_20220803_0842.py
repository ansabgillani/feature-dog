# Generated by Django 3.2.14 on 2022-08-03 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('posts', '0002_alter_post_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='commentupvote',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_upvotes', to='posts.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_tags', to='posts.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='users.organizationprofile'),
        ),
        migrations.AlterField(
            model_name='upvote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvotes', to='posts.post'),
        ),
    ]
