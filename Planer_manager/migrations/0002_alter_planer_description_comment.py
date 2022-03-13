# Generated by Django 4.0.3 on 2022-03-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Planer_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planer',
            name='description',
            field=models.TextField(max_length=150),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Planer_manager.planer')),
            ],
        ),
    ]