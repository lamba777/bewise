# Generated by Django 4.2.6 on 2023-10-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='previous_question',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
