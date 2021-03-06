# Generated by Django 2.1.2 on 2018-10-30 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto_Turistico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rank', models.FloatField(blank=True, default=0)),
            ],
        ),
    ]
