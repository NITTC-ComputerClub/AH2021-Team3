# Generated by Django 3.2.8 on 2021-10-30 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tadoku', '0003_auto_20211029_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='readbook',
            options={'verbose_name': 'Read Book', 'verbose_name_plural': 'Read Books'},
        ),
        migrations.AddField(
            model_name='readbook',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='readbook',
            name='read_at',
            field=models.DateField(),
        ),
    ]
