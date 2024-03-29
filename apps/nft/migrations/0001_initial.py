# Generated by Django 4.2.1 on 2023-07-25 18:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collections_nft', '0007_alter_collectionnft_previous_prices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='nft')),
                ('auction', models.BooleanField(default=False)),
                ('auction_end_date', models.DateTimeField(blank=True, null=True)),
                ('external_link', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('blockchain', models.CharField(choices=[('ETH', 'Ethereum')], max_length=3)),
                ('royalties', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('supply', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_nfts', to=settings.AUTH_USER_MODEL)),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_collections', to='collections_nft.collectionnft')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_nfts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
