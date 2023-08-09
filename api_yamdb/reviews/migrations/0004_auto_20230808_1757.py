# Generated by Django 3.2 on 2023-08-08 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_genres_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.categories'),
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genre',
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(null=True, related_name='titles', to='reviews.Genres'),
        ),
    ]
