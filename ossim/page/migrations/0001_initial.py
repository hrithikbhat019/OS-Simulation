# Generated by Django 2.0.2 on 2018-03-31 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MemSchedAlg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('demourl', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='adv',
            name='alg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.MemSchedAlg'),
        ),
    ]
