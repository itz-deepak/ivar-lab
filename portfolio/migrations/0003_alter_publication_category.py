# Generated by Django 3.2.9 on 2023-01-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20230123_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Journal', 'Journal'), ('Book Chapters', 'Book Chapters'), ('Books', 'Books'), ('International Reports', 'International Reports'), ('Conference', 'Conference')], default='Journal', max_length=60),
        ),
    ]
