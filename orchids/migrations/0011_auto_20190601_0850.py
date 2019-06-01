# Generated by Django 2.2.1 on 2019-06-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchids', '0010_auto_20190601_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='greenhouse',
            name='state',
            field=models.CharField(choices=[('NOT ASSIGNED', 'NOT ASSIGNED'), ('ASSIGNED', 'ASSIGNED'), ('SOLD', 'SOLD'), ('DESTROYED', 'DESTROYED')], default='NOT ASSIGNED', max_length=200),
        ),
        migrations.AlterField(
            model_name='greenhouse',
            name='weather',
            field=models.CharField(choices=[('ANDES', 'ANDES'), ('COAST', 'COAST')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orchid',
            name='preferred_weather',
            field=models.CharField(choices=[('ANDES', 'ANDES'), ('COAST', 'COAST')], default='', max_length=200),
        ),
    ]