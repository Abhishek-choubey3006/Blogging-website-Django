# Generated by Django 4.2.2 on 2024-05-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_post_author_image_alter_post_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('Inspiration', 'Inspiration'), ('Recent', 'Recent'), ('Tranding', 'Tranding'), ('main_post', 'main_post'), ('Latest_post', 'Latest_post'), ('Popular', 'Popular'), ('Editor_pick', 'Editor_pick')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('1', 'PUBLISH'), ('0', 'DRAFT')], max_length=100),
        ),
    ]