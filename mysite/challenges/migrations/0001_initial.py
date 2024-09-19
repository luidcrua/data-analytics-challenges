# Generated by Django 3.2.15 on 2024-09-18 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
            ],
        ),        
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('submitted_date_time', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ideas', to='challenges.creator')),
                ('times_shared', models.IntegerField()),
                ('votes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('views', models.IntegerField()),
                ('keywords', models.TextField(blank=True)),
            ],
        ),
    ]
