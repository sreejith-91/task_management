# Generated by Django 3.0.5 on 2021-01-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='commented_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admins site.'),
        ),
    ]
