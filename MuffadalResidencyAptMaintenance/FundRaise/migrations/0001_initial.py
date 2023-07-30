# Generated by Django 4.2 on 2023-07-23 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Expense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundRaiseModel',
            fields=[
                ('expensemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Expense.expensemodel')),
            ],
            bases=('Expense.expensemodel',),
        ),
    ]