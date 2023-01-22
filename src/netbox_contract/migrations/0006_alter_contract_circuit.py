# Generated by Django 4.1.5 on 2023-01-22 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("circuits", "0041_standardize_description_comments"),
        ("netbox_contract", "0005_contract_accounting_dimensions_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="circuit",
            field=models.ManyToManyField(
                blank=True, related_name="contracts", to="circuits.circuit"
            ),
        ),
    ]
