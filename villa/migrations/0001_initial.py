# Generated by Django 5.0.4 on 2024-04-26 05:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/villa_image/')),
                ('area', models.PositiveSmallIntegerField(help_text='m2')),
                ('security', models.PositiveSmallIntegerField(choices=[(1, 'Охроняемая территория'), (2, 'Не охроняемая территория')])),
                ('description', models.TextField()),
                ('floor_number', models.PositiveSmallIntegerField()),
                ('bedroom', models.PositiveSmallIntegerField()),
                ('bathroom', models.PositiveSmallIntegerField()),
                ('parking_space_capacity', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=30)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.category')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.material')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='villa.paymentmethod')),
            ],
        ),
    ]
