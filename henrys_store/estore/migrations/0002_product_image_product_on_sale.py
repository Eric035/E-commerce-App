# Generated by Django 4.0.4 on 2022-05-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
