# Generated by Django 3.2.3 on 2021-05-22 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books.publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='books.series'),
        ),
    ]