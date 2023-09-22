# Generated by Django 4.2.5 on 2023-09-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nest", "0004_alter_apartment_apartment_expense_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apartment",
            name="cost_to_rent",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]