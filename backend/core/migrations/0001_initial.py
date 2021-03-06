# Generated by Django 3.1.4 on 2020-12-17 21:39

import core.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(default=datetime.datetime(2020, 12, 17, 21, 39, 47, 203418, tzinfo=utc), editable=False)),
                ('start_date_requested', models.DateTimeField(validators=[core.models.validate_time])),
                ('end_date_requested', models.DateTimeField(validators=[core.models.validate_time])),
                ('quoted_price', models.CharField(max_length=50)),
                ('final_cost', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
                ('accepted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.users')),
            ],
        ),
    ]
