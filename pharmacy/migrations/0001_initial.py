# Generated by Django 2.2.1 on 2019-05-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharm_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('medicines', models.BinaryField()),
            ],
        ),
    ]
