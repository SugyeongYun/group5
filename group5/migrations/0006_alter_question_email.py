# Generated by Django 4.0.3 on 2023-05-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group5', '0005_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
