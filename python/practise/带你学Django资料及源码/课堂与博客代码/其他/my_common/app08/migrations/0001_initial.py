# Generated by Django 2.1.5 on 2019-12-26 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品名字')),
                ('content', models.TextField(verbose_name='商品名字')),
            ],
        ),
    ]
