# Generated by Django 3.2.3 on 2021-06-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_mascotas_img_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='img_mascota',
            field=models.ImageField(null=True, upload_to='static/media/mascota'),
        ),
    ]
