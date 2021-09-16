# Generated by Django 3.2.5 on 2021-09-13 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Deactive'), (1, 'Active')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('project_info', models.CharField(blank=True, max_length=200, null=True)),
                ('client_name', models.CharField(blank=True, max_length=200, null=True)),
                ('industry', models.CharField(blank=True, max_length=200, null=True)),
                ('technology', models.CharField(blank=True, max_length=200, null=True)),
                ('link_title_name', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Deactive'), (1, 'Active')], default=1)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprofile.category')),
            ],
        ),
    ]