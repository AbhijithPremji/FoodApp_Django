# Generated by Django 5.0.3 on 2024-03-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FooBack', '0002_itemsdb_date_data_newcatdb_data_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsdb',
            name='Category',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
