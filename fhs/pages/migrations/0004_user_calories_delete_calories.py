# Generated by Django 4.0.2 on 2022-03-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_calories'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Calories',
        ),
    ]
