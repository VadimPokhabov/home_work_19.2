# Generated by Django 4.2 on 2024-05-24 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(default=1, verbose_name='Номер версии')),
                ('name_version', models.CharField(max_length=250, verbose_name='Имя версии')),
                ('version_flag', models.BooleanField(default=False, verbose_name='Признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='catalog.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
