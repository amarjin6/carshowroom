# Generated by Django 4.0.6 on 2022-08-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_sender_customerorder_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='last_update',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='dealerorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dealerorder',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dealerorder',
            name='last_update',
            field=models.DateTimeField(blank=True),
        ),
    ]
