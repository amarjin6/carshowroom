# Generated by Django 4.0.6 on 2022-08-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_customerorder_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dealerorder',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]