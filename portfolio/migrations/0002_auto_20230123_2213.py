# Generated by Django 3.2.9 on 2023-01-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Journal', 'Journal'), ('Conference', 'Conference'), ('Books', 'Books'), ('International Reports', 'International Reports'), ('Book Chapters', 'Book Chapters')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='reasearch',
            name='category',
            field=models.CharField(choices=[('Invited Talks', 'Invited Talks'), ('Editorial Boards', 'Editorial Boards'), ('Conference Presentation', 'Conference Presentation')], default='Invited Talks', max_length=60),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('Team', 'Team'), ('Alumini', 'Alumini')], default='Team', max_length=60),
        ),
    ]