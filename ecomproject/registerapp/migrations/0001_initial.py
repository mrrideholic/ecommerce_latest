# Generated by Django 4.2 on 2023-06-17 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.BooleanField()),
                ('debit', models.BooleanField()),
                ('credit', models.BooleanField()),
                ('emi', models.BooleanField()),
            ],
        ),
    ]