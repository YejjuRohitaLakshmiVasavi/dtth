# Generated by Django 4.1.7 on 2023-05-09 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('airline', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
