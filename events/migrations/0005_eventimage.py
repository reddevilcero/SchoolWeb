# Generated by Django 2.0.3 on 2019-02-25 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190225_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/events', verbose_name='Event Images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Event Image',
                'verbose_name_plural': 'Event Images',
            },
        ),
    ]
