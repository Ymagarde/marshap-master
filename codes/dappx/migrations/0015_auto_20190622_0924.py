# Generated by Django 2.2 on 2019-06-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0014_auto_20190212_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notify_email',
            field=models.EmailField(blank=True, max_length=512, null=True),
        ),
    ]
