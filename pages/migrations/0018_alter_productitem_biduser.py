# Generated by Django 4.0.2 on 2022-09-20 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_productitem_biduser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='biduser',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
