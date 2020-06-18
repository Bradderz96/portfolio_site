# Generated by Django 3.0.6 on 2020-05-31 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_site', '0003_suggestions_vote_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_info', models.CharField(max_length=1000)),
                ('project_link', models.CharField(max_length=200)),
            ],
        ),
    ]