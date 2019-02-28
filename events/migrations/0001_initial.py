# Generated by Django 2.0.3 on 2019-02-24 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BaseModel')),
                ('title', models.CharField(max_length=100, verbose_name='Event Name')),
                ('time', models.DateTimeField(verbose_name='Event Time')),
                ('place', models.CharField(max_length=100, verbose_name='Event Place')),
                ('postcode', models.CharField(max_length=10, verbose_name='Event Postcode')),
                ('link', models.URLField(verbose_name='Google Maps Link to Event')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('linked_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='events.Event')),
            ],
            options={
                'verbose_name': 'Event Image',
                'verbose_name_plural': 'Event Images',
            },
        ),
    ]
