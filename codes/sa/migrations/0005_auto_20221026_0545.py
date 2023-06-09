# Generated by Django 2.2.16 on 2022-10-26 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sa', '0004_auto_20221026_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('device_timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sa.Session')),
            ],
        ),
        migrations.DeleteModel(
            name='GpsEntry',
        ),
    ]
