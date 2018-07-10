# Generated by Django 2.0.7 on 2018-07-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('description', models.TextField()),
                ('link', models.CharField(blank=True, max_length=127)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('summary', models.TextField()),
                ('details', models.TextField()),
                ('website', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField(blank=True)),
                ('link', models.CharField(blank=True, max_length=200)),
                ('citation', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=63)),
                ('last_name', models.CharField(max_length=63)),
                ('title', models.CharField(max_length=127)),
                ('bio', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('last_name', 'first_name'),
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='staff',
            field=models.ManyToManyField(blank=True, to='content.StaffMember'),
        ),
        migrations.AddField(
            model_name='project',
            name='publications',
            field=models.ManyToManyField(blank=True, to='content.Publication'),
        ),
        migrations.AddField(
            model_name='project',
            name='staff',
            field=models.ManyToManyField(blank=True, to='content.StaffMember'),
        ),
    ]