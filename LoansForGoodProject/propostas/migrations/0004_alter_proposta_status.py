# Generated by Django 4.2.4 on 2023-09-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propostas', '0003_configuracaocampos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='status',
            field=models.CharField(choices=[('análise humana', 'análise humana'), ('Aprovada', 'Aprovada'), ('Negada', 'Negada')], default='análise humana', max_length=20),
        ),
    ]
