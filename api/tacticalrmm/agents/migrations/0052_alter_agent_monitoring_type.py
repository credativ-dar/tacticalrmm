# Generated by Django 4.0.4 on 2022-05-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0051_alter_agent_plat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='monitoring_type',
            field=models.CharField(choices=[('server', 'Server'), ('workstation', 'Workstation')], default='server', max_length=30),
        ),
    ]