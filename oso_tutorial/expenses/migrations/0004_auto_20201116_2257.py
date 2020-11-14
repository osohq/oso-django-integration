# Generated by Django 3.1 on 2020-11-16 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20201114_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymember',
            old_name='user',
            new_name='member',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.AddField(
            model_name='categorymember',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='expenses.organization'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymember',
            name='role',
            field=models.CharField(default='NA', max_length=64),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='member', max_length=64)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(through='expenses.OrganizationMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='organizations',
            field=models.ManyToManyField(related_name='member', through='expenses.OrganizationMember', to='expenses.Organization'),
        ),
    ]
