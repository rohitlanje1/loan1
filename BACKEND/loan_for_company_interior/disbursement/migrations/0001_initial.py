# Generated by Django 4.1.6 on 2023-02-11 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loan_sanctioning', '0001_initial'),
        ('application_generation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=250)),
                ('vendor_type', models.CharField(blank=True, default=0, max_length=250)),
                ('email', models.EmailField(blank=True, default=0, max_length=254)),
                ('address', models.TextField(blank=True, default=0, max_length=250)),
                ('city', models.CharField(blank=True, default=0, max_length=250)),
                ('state', models.CharField(blank=True, default=0, max_length=250)),
                ('country', models.CharField(blank=True, default=0, max_length=250)),
                ('pin_code', models.IntegerField(blank=True, default=0)),
                ('mobile', models.CharField(blank=True, default=0, max_length=10)),
                ('bank_name', models.CharField(blank=True, default=0, max_length=250)),
                ('passbook_copy', models.FileField(blank=True, default=0, upload_to='customer/vendor/')),
                ('current_account_no', models.CharField(blank=True, default=0, max_length=25)),
                ('ifsc_code', models.CharField(blank=True, default=0, max_length=20)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendors', to='application_generation.application')),
            ],
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_amount', models.FloatField(blank=True, default=0)),
                ('installment_no', models.IntegerField(blank=True, default=0)),
                ('monthly_installment_amount', models.FloatField(blank=True, default=0)),
                ('installment_expected_date', models.DateField(blank=True, default='2000-12-12')),
                ('installment_paid_date', models.DateField(blank=True, default='2000-12-12')),
                ('penalty_amount', models.FloatField(blank=True, default=0)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'pending')], default='pending', max_length=100)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Installments', to='loan_sanctioning.loan')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_doc', models.FileField(blank=True, default=0, upload_to='media/customer/disbursement')),
                ('payment_mode', models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('UPI', 'UPI')], default=0, max_length=250)),
                ('net_disbursed_amount', models.FloatField(blank=True, default=0)),
                ('disbursed_to_account_no', models.CharField(blank=True, default=0, max_length=25)),
                ('receipt_doc', models.FileField(blank=True, default=0, upload_to='customer/disbursement')),
                ('status', models.CharField(blank=True, choices=[('In_process', 'In_process'), ('Pending', 'Pending')], default=0, max_length=250)),
                ('response_timestamp', models.DateTimeField(auto_now=True)),
                ('loan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Disbursements', to='loan_sanctioning.loan')),
            ],
        ),
    ]
