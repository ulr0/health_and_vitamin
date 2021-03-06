# Generated by Django 3.1.7 on 2021-04-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='ShippingInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=2000)),
                ('phone_number', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'shipping_informations',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('coupons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.coupon')),
                ('payment_methods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.paymentmethod')),
                ('shipping_informations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.shippinginformation')),
                ('statuses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.status')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'carts',
            },
        ),
    ]
