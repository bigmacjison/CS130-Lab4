# Generated by Django 2.0.4 on 2018-04-18 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_code', models.CharField(max_length=10)),
                ('total_price', models.FloatField(default=0)),
                ('cart_paid', models.BooleanField(default=False)),
                ('cart_created', models.DateTimeField(verbose_name='date created')),
                ('cart_updated', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_price', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=200)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_text', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('shipping_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.User'),
        ),
    ]
