# Generated by Django 4.1.5 on 2023-01-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('netbox_contract', '0009_contract_external_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='contracts',
            field=models.ManyToManyField(
                blank=True, related_name='invoices', to='netbox_contract.contract'
            ),
        ),
    ]
