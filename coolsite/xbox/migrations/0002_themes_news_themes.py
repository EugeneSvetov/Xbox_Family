# Generated by Django 4.1 on 2022-09-11 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Игры', 'games'), ('Xbox', 'Xbox'), ('Оффтоп', 'off')], max_length=6)),
            ],
            options={
                'verbose_name': 'Тэги',
                'verbose_name_plural': 'Тэг',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='themes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='xbox.themes'),
        ),
    ]
