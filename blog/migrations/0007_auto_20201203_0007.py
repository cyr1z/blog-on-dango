# Generated by Django 3.1.3 on 2020-12-03 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Categories',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tag_posts', to='blog.Tag'),
        ),
    ]
