# Generated by Django 4.2.6 on 2023-11-07 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(upload_to='blog/', verbose_name='Изображение'),
        ),
    ]
