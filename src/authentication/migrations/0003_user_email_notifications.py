# Generated by Django 3.2.3 on 2021-09-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210906_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_notifications',
            field=models.BooleanField(default=False, verbose_name='Email подписка на рассылку'),
        ),
    ]