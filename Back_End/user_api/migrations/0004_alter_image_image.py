# Generated by Django 4.1.5 on 2024-03-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_api', '0003_remove_image_uploaded_at_remove_image_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(default='', upload_to='posts/'),
        ),
    ]
