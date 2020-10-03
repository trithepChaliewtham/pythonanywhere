# Generated by Django 3.0.3 on 2020-10-03 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Farm_Name', models.CharField(default='ชื่อฟาร์ม', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('SeasonName', models.CharField(default='ฤดูร้อน', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fruit_Name', models.CharField(default='Banana', max_length=100)),
                ('Price', models.FloatField()),
                ('FarmName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Farm')),
                ('Season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Season')),
            ],
        ),
    ]
