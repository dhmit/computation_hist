# Generated by Django 2.1.5 on 2019-03-08 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0022_remove_page_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_name',
            field=models.CharField(blank=True, max_length=191, unique=True),
        ),
    ]
