# Generated by Django 2.0.7 on 2018-07-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180711_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-create_date'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_created',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_published',
            new_name='publish_date',
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
