# Generated by Django 3.1.7 on 2021-04-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
            ],
            options={
                'db_table': 'discounts',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'options',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.IntegerField()),
                ('detail', models.TextField()),
                ('stock', models.IntegerField()),
                ('expired_at', models.DateField()),
                ('is_hit', models.BooleanField(default=0)),
                ('is_option', models.BooleanField(default=0)),
                ('discounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.discount')),
                ('options', models.ManyToManyField(through='products.Option', to='products.Product')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ShippingFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('minimum_free', models.IntegerField()),
            ],
            options={
                'db_table': 'shipping_fees',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('main_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.maincategory')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('sub_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
            options={
                'db_table': 'sub_category_products',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_fees',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shippingfee'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_cateories',
            field=models.ManyToManyField(through='products.SubCategory_Product', to='products.SubCategory'),
        ),
        migrations.AddField(
            model_name='option',
            name='options',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product_option', to='products.product'),
        ),
        migrations.AddField(
            model_name='option',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='products.product'),
        ),
        migrations.AddField(
            model_name='maincategory',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.menu'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]
