# Generated by Django 4.0.6 on 2022-08-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0004_alter_dealer_created_at_alter_dealer_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dealercar',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]