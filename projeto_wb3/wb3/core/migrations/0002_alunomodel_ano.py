# Generated by Django 4.1.3 on 2022-12-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunomodel',
            name='ano',
            field=models.IntegerField(default=1, verbose_name='Ano'),
            preserve_default=False,
        ),
    ]
