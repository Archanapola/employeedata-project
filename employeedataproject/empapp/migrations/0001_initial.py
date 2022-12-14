# Generated by Django 3.1 on 2022-10-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('salary', models.IntegerField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
