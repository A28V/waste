# Generated by Django 4.1.7 on 2023-04-30 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pic1', models.ImageField(upload_to='catalog/')),
                ('pic2', models.ImageField(upload_to='catalog/')),
                ('pic3', models.ImageField(upload_to='catalog/')),
                ('pic4', models.ImageField(upload_to='catalog/')),
                ('mrp', models.IntegerField()),
                ('sellingprice', models.IntegerField()),
                ('description', models.CharField(max_length=800)),
                ('specification', models.CharField(default='', max_length=600)),
                ('tag', models.CharField(choices=[('new', 'new'), ('top', 'top'), ('best', 'best'), ('featured', 'featured'), ('popular', 'popular'), ('trending', 'trending'), ('awesome', 'awesome'), ('beautiful', 'beautiful'), ('stlish', 'stylish')], max_length=200)),
                ('available', models.CharField(choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'), ('Preorder', 'Preorder')], max_length=200)),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoryname', to='catalog_settings.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
