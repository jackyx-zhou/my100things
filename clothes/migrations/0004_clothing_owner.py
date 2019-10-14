# Generated by Django 2.2.5 on 2019-10-13 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0003_auto_20191009_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clothing', to=settings.AUTH_USER_MODEL),
        ),
    ]
