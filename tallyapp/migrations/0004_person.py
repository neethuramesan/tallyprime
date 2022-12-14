# Generated by Django 4.0.5 on 2022-08-01 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tallyapp', '0003_tds_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('pan', models.CharField(max_length=255)),
                ('flatno', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('road', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('std', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tallyapp.companies')),
            ],
        ),
    ]
