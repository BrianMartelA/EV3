# Generated by Django 5.0.6 on 2024-06-14 03:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alter_cliente_confirmmail_alter_cliente_mail'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='confirmmail',
            field=models.CharField(default='default@example.com', max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='mail',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Registro_cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]