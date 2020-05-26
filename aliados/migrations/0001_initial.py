# Generated by Django 3.0.6 on 2020-05-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aliado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('poder', models.CharField(max_length=100)),
                ('mundo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Aliados',
            },
        ),
    ]
