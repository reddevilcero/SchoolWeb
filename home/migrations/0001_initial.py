# Generated by Django 2.0.3 on 2019-02-15 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('image', models.ImageField(upload_to='img/slice', verbose_name='Image')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('rol', models.CharField(max_length=50, verbose_name='Occupation')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Quick Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/tutors', verbose_name='Profile Image')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter Link')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram Link')),
            ],
            bases=('core.basemodel',),
        ),
    ]
