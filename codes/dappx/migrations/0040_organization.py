# Generated by Django 2.2.13 on 2021-06-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0039_auto_20210622_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]