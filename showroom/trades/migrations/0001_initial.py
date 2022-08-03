# Generated by Django 4.0.6 on 2022-08-03 18:24

import core.enums
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('RUB', 'Ruble'), ('PLN', 'Zloty'), ('UAH', 'Hryvnia'), ('JPY', 'Yen'), ('CNY', 'Yuan'), ('TRY', 'Turkish Lira'), ('ITL', 'Lira'), ('BTC', 'Bitcoin')], default=core.enums.Acronym['USD'], max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_balance', to='trades.currency')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_balance', to='users.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
