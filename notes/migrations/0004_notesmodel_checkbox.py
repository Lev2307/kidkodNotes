# Generated by Django 3.2 on 2022-04-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20220415_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesmodel',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
    ]
