from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='album',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='image_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='album',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
