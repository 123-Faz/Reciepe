# Generated by Django 5.1.4 on 2024-12-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reciepe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reciepe_name', models.CharField(max_length=100)),
                ('Reciepe_description', models.TextField()),
                ('Reciepe_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
