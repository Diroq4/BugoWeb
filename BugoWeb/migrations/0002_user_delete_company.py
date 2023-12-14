# Generated by Django 5.0 on 2023-12-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BugoWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
