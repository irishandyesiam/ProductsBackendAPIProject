# Generated by Django 4.1 on 2022-08-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('comments', models.CharField(max_length=255)),
                ('product_id', models.IntegerField()),
            ],
        ),
    ]
