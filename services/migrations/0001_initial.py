# Generated by Django 5.1.3 on 2024-11-30 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('Installation', 'Installation'), ('Repair', 'Repair'), ('Inquiry', 'Inquiry')], max_length=50)),
                ('description', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.customer')),
            ],
        ),
    ]
