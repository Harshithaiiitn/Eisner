# Generated by Django 2.1.12 on 2019-09-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJ', '0013_controls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessactivity',
            name='businessdefinition_q',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='regulations',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='regulations',
            name='regulation',
            field=models.TextField(),
        ),
    ]
