# Generated by Django 4.2.5 on 2023-09-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staffdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Position', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=5, max_digits=20)),
                ('City', models.CharField(max_length=15)),
            ],
        ),
    ]
