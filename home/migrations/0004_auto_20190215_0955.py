# Generated by Django 2.0.3 on 2019-02-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_tutor_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='title',
            field=models.CharField(blank=True, choices=[('Prof.', 'Prof.'), ('Dr.', 'Dr.'), ('Mr.', 'Mr'), ('Mrs.', 'Mrs'), ('Ms.', 'Ms')], max_length=25, null=True, verbose_name='Title'),
        ),
    ]
