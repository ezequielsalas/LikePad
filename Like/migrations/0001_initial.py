# Generated by Django 2.0.6 on 2018-06-15 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes_given', to=settings.AUTH_USER_MODEL)),
                ('reported_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]