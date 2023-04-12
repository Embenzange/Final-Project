# Generated by Django 4.1.7 on 2023-03-29 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('waitingapproval', 'Waiting approval'), ('active', 'Actve'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]
