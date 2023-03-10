# Generated by Django 4.1.4 on 2023-01-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='student')),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('CPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(blank=True, max_length=100, null=True)),
                ('CDesc', models.CharField(blank=True, max_length=100, null=True)),
                ('CImage', models.ImageField(blank=True, null=True, upload_to='category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat', models.CharField(blank=True, max_length=100, null=True)),
                ('Pro', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Desc', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='product')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Gender', models.CharField(blank=True, max_length=10, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='student')),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
