# Generated by Django 3.2.11 on 2022-06-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0010_alter_application_nom_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='nom_app',
            field=models.CharField(max_length=20),
        ),
    ]