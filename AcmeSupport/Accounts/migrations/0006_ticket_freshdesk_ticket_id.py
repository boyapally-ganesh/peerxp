# Generated by Django 4.0.1 on 2023-07-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='freshdesk_ticket_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
