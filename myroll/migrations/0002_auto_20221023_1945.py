# Generated by Django 3.2.15 on 2022-10-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('userpk', models.IntegerField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]