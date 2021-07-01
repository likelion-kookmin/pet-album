# Generated by Django 3.2.4 on 2021-06-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('comment', models.TextField(blank=True)),
                ('image_datetime', models.DateField()),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
    ]
