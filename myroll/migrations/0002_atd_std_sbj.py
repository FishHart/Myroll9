# Generated by Django 3.2.15 on 2022-11-20 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myroll', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='atd',
            constraint=models.UniqueConstraint(fields=('std_id', 'sbj_name'), name='std_sbj'),
        ),
    ]