# Generated by Django 4.0.3 on 2022-03-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shop', '0002_alter_book_options_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/image/'),
        ),
    ]
