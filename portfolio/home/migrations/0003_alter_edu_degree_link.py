# Generated by Django 4.1.11 on 2023-10-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_edu_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='degree_link',
            field=models.FileField(default=None, null=True, upload_to='degree'),
        ),
    ]
