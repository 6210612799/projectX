# Generated by Django 3.2.8 on 2021-10-28 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('detail', models.CharField(max_length=256)),
                ('amount', models.IntegerField(default=4)),
                ('count', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owners', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
