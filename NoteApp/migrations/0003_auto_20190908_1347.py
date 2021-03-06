# Generated by Django 2.2.5 on 2019-09-08 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NoteApp', '0002_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='Note',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='NoteApp.Category'),
        ),
        migrations.AlterField(
            model_name='Note',
            name='text',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
