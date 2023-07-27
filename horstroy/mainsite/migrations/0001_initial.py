# Generated by Django 4.2.3 on 2023-07-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('descriptipon', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='services', verbose_name='Картинка')),
                ('gallery', models.ManyToManyField(related_name='gallery', to='mainsite.image', verbose_name='Галерея')),
            ],
        ),
    ]