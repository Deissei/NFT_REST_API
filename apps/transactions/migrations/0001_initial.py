# Generated by Django 4.2.1 on 2023-07-28 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nft', '0002_alter_nft_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(choices=[('Покупка', 'Покупка'), ('Продажа', 'Продажа')], max_length=7)),
                ('status', models.CharField(choices=[('В ожидании', 'В ожидании'), ('Успешно завершено', 'Успешно завершено')], max_length=17)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_buyer', to=settings.AUTH_USER_MODEL)),
                ('nft_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_nft', to='nft.nft')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-transaction_date'],
            },
        ),
    ]
