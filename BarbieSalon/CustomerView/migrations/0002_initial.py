# Generated by Django 4.1.4 on 2023-01-03 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CustomerView', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homeslideimg',
            name='images',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.homedetails'),
        ),
        migrations.AddField(
            model_name='businessdata',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.navbar'),
        ),
    ]