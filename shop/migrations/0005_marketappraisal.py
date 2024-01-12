# Generated by Django 5.0 on 2024-01-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orderupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketAppraisal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=3)),
                ('bedrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('bathrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('cars', models.PositiveIntegerField(blank=True, null=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]