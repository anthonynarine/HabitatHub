# Generated by Django 4.2.5 on 2023-09-21 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nest", "0008_alter_apartment_options_alter_floor_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apartment",
            options={"ordering": ["apartment_number"]},
        ),
        migrations.AlterModelOptions(
            name="floor",
            options={"ordering": ["floor_number"]},
        ),
    ]
