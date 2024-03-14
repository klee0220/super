# Generated by Django 5.0.3 on 2024-03-14 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FieldAnalyzer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(max_length=100)),
                ('urgency', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('analyzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.fieldanalyzer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='fieldanalyzer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_app.user'),
        ),
    ]
