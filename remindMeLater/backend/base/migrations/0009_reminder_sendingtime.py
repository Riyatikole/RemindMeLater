# Generated by Django 4.2.11 on 2024-03-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_reminder_sendingdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='sendingTime',
            field=models.TextField(null=True),
        ),
    ]
