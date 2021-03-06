# Generated by Django 2.1.3 on 2018-12-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countrydata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={},
        ),
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='country',
            order_with_respect_to='name',
        ),
    ]
