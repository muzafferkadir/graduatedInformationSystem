# Generated by Django 2.2.3 on 2019-07-28 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_auto_20190725_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_to_me', to=settings.AUTH_USER_MODEL),
        ),
    ]
