# Generated by Django 4.2.2 on 2024-05-31 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_finance_section_alter_finance_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagsfinance',
            name='post',
        ),
        migrations.AlterField(
            model_name='finance',
            name='section',
            field=models.CharField(choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Latest_post', 'Latest_post'), ('Inspiration', 'Inspiration'), ('Editor_pick', 'Editor_pick'), ('main_post', 'main_post'), ('Tranding', 'Tranding')], max_length=200),
        ),
        migrations.AlterField(
            model_name='finance',
            name='status',
            field=models.CharField(choices=[('0', 'DRAFT'), ('1', 'PUBLISH')], max_length=100),
        ),
        migrations.AlterField(
            model_name='political',
            name='section',
            field=models.CharField(choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Latest_post', 'Latest_post'), ('Inspiration', 'Inspiration'), ('Editor_pick', 'Editor_pick'), ('main_post', 'main_post'), ('Tranding', 'Tranding')], max_length=200),
        ),
        migrations.AlterField(
            model_name='political',
            name='status',
            field=models.CharField(choices=[('0', 'DRAFT'), ('1', 'PUBLISH')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('Popular', 'Popular'), ('Recent', 'Recent'), ('Latest_post', 'Latest_post'), ('Inspiration', 'Inspiration'), ('Editor_pick', 'Editor_pick'), ('main_post', 'main_post'), ('Tranding', 'Tranding')], max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('0', 'DRAFT'), ('1', 'PUBLISH')], max_length=100),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='Tagsfinance',
        ),
    ]
