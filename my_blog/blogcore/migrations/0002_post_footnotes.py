# Generated by Django 4.1.6 on 2023-02-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='footnotes',
            field=models.TextField(blank=True),
        ),
    ]