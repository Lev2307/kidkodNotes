# Generated by Django 3.2 on 2022-04-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesmodel',
            name='body',
            field=models.TextField(max_length=200),
        ),
    ]
