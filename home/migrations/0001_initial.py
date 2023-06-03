# Generated by Django 4.2.1 on 2023-06-03 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auther', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
            ],
            options={
                'verbose_name_plural': 'users',
            },
        ),
    ]
