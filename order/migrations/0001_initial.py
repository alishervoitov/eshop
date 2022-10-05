# Generated by Django 4.0 on 2022-03-10 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('expired_date', models.DateTimeField(null=True)),
                ('required_date', models.DateTimeField(null=True)),
                ('shipped_date', models.DateTimeField(null=True)),
                ('canceled_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('INPROGRESS', 'inprogress'), ('COMPLATED', 'complated'), ('CANCELED', 'canceled')], default='PENDING', max_length=10)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='product.product')),
            ],
        ),
    ]
