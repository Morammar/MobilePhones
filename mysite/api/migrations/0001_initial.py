# Generated by Django 4.2.9 on 2024-02-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]