# Generated by Django 4.0.1 on 2022-01-13 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=18)),
                ('typ_account', models.CharField(choices=[('c', 'Carteira'), ('cc', 'Conta Corrente'), ('p', 'Poupança')], max_length=2)),
                ('inst_finaceira', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=18)),
                ('dRecebimento', models.DateField()),
                ('dRe_Esperado', models.DateField()),
                ('desc', models.TextField()),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conta', to='main.conta')),
            ],
        ),
    ]