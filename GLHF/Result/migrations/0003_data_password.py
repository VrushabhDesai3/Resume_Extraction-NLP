# Generated by Django 3.0.2 on 2020-02-02 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Result', '0002_auto_20200202_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='password',
            field=models.CharField(default='abcd', max_length=10),
            preserve_default=False,
        ),
    ]