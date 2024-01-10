# Generated by Django 4.2.6 on 2023-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('mob_num', models.IntegerField()),
                ('message', models.TextField(max_length=30)),
            ],
        ),
    ]