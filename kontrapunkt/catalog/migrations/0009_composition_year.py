# Generated by Django 2.2.6 on 2020-03-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_composition_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='year',
            field=models.CharField(default='', help_text='Year as text', max_length=12),
        ),
    ]