# Generated by Django 4.2.11 on 2024-03-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_reminder_reminder_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='createdAt',
            field=models.DateField(null=True),
        ),
    ]
