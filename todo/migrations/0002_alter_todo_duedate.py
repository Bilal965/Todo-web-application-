# Generated by Django 4.1.3 on 2022-11-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]