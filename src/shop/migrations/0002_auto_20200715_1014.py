# Generated by Django 3.0.8 on 2020-07-15 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]