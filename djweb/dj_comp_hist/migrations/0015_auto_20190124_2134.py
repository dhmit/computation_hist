# Generated by Django 2.1.5 on 2019-01-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_comp_hist', '0014_document_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
