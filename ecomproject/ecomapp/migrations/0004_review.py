# Generated by Django 4.2 on 2023-06-21 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_product_image1_product_image2_product_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('review', models.TextField()),
                ('rate', models.TextField()),
            ],
        ),
    ]
