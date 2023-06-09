# Generated by Django 2.2.16 on 2022-10-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0005_auto_20221026_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='gpsc',
            name='device',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='session',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sa.Device'),
        ),
        migrations.AddField(
            model_name='sessionpoint',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sa.Device'),
        ),
    ]
