# Generated by Django 3.2.5 on 2021-07-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='vote_average',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
