# Generated by Django 3.1.6 on 2022-03-20 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugapp', '0005_auto_20220320_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_lead', to='bugapp.userprofile'),
        ),
    ]