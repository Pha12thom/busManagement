# Generated by Django 4.2.10 on 2024-02-23 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0004_alter_bus_departure_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='bus',
            name='arrival_city',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Mombasa', 'Mombasa'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya'), ('Meru', 'Meru'), ('Kisii', 'Kisii'), ('Narok', 'Narok'), ('Nyeri', 'Nyeri'), ('Thika', 'Thika'), ('Turkana', 'Turkana')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='departure_city',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Mombasa', 'Mombasa'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya'), ('Meru', 'Meru'), ('Kisii', 'Kisii'), ('Narok', 'Narok'), ('Nyeri', 'Nyeri'), ('Thika', 'Thika'), ('Turkana', 'Turkana')], max_length=150),
        ),
    ]
