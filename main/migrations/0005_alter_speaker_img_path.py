# Generated by Django 4.2 on 2023-05-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_speaker_id_conversation_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='img_path',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
