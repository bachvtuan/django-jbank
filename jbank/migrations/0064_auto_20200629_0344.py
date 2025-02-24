# Generated by Django 3.0.6 on 2020-06-29 03:44

from django.db import migrations
import jutil.modelfields
import jutil.validators


class Migration(migrations.Migration):

    dependencies = [
        ("jbank", "0063_auto_20200608_1827"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currencyexchange",
            name="source_currency",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=3, verbose_name="source currency"),
        ),
        migrations.AlterField(
            model_name="currencyexchange",
            name="target_currency",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=3, verbose_name="target currency"),
        ),
        migrations.AlterField(
            model_name="currencyexchange",
            name="unit_currency",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=3, verbose_name="unit currency"),
        ),
        migrations.AlterField(
            model_name="currencyexchangesource",
            name="name",
            field=jutil.modelfields.SafeCharField(max_length=64, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="file_name",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, editable=False, max_length=255, verbose_name="file name"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="file_reference",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, editable=False, max_length=255, verbose_name="file reference"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="full_path",
            field=jutil.modelfields.SafeTextField(blank=True, editable=False, verbose_name="full path"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="messages",
            field=jutil.modelfields.SafeTextField(blank=True, default="", verbose_name="recipient messages"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="msg_id",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, editable=False, max_length=64, verbose_name="message id"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="reference",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=32, verbose_name="recipient reference"),
        ),
        migrations.AlterField(
            model_name="payout",
            name="state",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[
                    ("W", "waiting processing"),
                    ("U", "waiting upload"),
                    ("D", "uploaded"),
                    ("P", "paid"),
                    ("C", "canceled"),
                    ("E", "error"),
                ],
                db_index=True,
                default="W",
                max_length=1,
                verbose_name="state",
            ),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="account_number",
            field=jutil.modelfields.SafeCharField(
                db_index=True,
                max_length=35,
                validators=[jutil.validators.iban_validator],
                verbose_name="account number",
            ),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="address",
            field=jutil.modelfields.SafeTextField(blank=True, default="", verbose_name="address"),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="bic",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=16, verbose_name="BIC"),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="country_code",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="FI", max_length=2, verbose_name="country code"),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="name",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=128, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="payoutparty",
            name="org_id",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=32, verbose_name="organization id"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="file_name",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, editable=False, max_length=128, verbose_name="file name"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="file_path",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, editable=False, max_length=255, verbose_name="file path"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="group_status",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=8, verbose_name="group status"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="msg_id",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=64, verbose_name="message id"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="original_msg_id",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=64, verbose_name="original message id"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="response_code",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=4, verbose_name="response code"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="response_text",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=128, verbose_name="response text"),
        ),
        migrations.AlterField(
            model_name="payoutstatus",
            name="status_reason",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=255, verbose_name="status reason"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatch",
            name="currency_identifier",
            field=jutil.modelfields.SafeCharField(choices=[("1", "EUR")], max_length=3, verbose_name="currency identifier"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatch",
            name="institution_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=2, verbose_name="institution identifier"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatch",
            name="service_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=9, verbose_name="service identifier"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatchfile",
            name="errors",
            field=jutil.modelfields.SafeTextField(blank=True, default="", max_length=4086, verbose_name="errors"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatchfile",
            name="original_filename",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=256, verbose_name="original filename"),
        ),
        migrations.AlterField(
            model_name="referencepaymentbatchfile",
            name="tag",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=64, verbose_name="tag"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="account_number",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=32, verbose_name="account number"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="archive_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=32, verbose_name="archive identifier"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="correction_identifier",
            field=jutil.modelfields.SafeCharField(
                choices=[("0", "Regular Entry"), ("1", "Correction Entry")],
                max_length=1,
                verbose_name="correction identifier",
            ),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="currency_identifier",
            field=jutil.modelfields.SafeCharField(choices=[("1", "EUR")], max_length=1, verbose_name="currency identifier"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="delivery_method",
            field=jutil.modelfields.SafeCharField(
                choices=[("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                db_index=True,
                max_length=1,
                verbose_name="delivery method",
            ),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="name_source",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[("", "Not Set"), ("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                max_length=1,
                verbose_name="name source",
            ),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="payer_name",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=12, verbose_name="payer name"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="receipt_code",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[("", ""), ("E", "Separate"), ("P", "Separate/Paper")],
                db_index=True,
                max_length=1,
                verbose_name="receipt code",
            ),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="record_type",
            field=jutil.modelfields.SafeCharField(max_length=1, verbose_name="record type"),
        ),
        migrations.AlterField(
            model_name="referencepaymentrecord",
            name="remittance_info",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=32, verbose_name="remittance info"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="account_name",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=32, verbose_name="account name"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="account_number",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=32, verbose_name="account number"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="bank_specific_info_1",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=1024, verbose_name="bank specific info (1)"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="bic",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=11, verbose_name="BIC"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="contact_info_1",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=64, verbose_name="contact info (1)"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="contact_info_2",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=64, verbose_name="contact info (2)"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="currency_code",
            field=jutil.modelfields.SafeCharField(max_length=3, verbose_name="currency code"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="customer_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=64, verbose_name="customer identifier"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="iban",
            field=jutil.modelfields.SafeCharField(db_index=True, max_length=32, verbose_name="IBAN"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="owner_name",
            field=jutil.modelfields.SafeCharField(max_length=64, verbose_name="owner name"),
        ),
        migrations.AlterField(
            model_name="statement",
            name="statement_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=48, verbose_name="statement identifier"),
        ),
        migrations.AlterField(
            model_name="statementfile",
            name="errors",
            field=jutil.modelfields.SafeTextField(blank=True, default="", max_length=4086, verbose_name="errors"),
        ),
        migrations.AlterField(
            model_name="statementfile",
            name="original_filename",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=256, verbose_name="original filename"),
        ),
        migrations.AlterField(
            model_name="statementfile",
            name="tag",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=64, verbose_name="tag"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="archive_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=64, verbose_name="archive identifier"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="bank_messages",
            field=jutil.modelfields.SafeTextField(blank=True, default="", verbose_name="bank messages"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="client_messages",
            field=jutil.modelfields.SafeTextField(blank=True, default="", verbose_name="client messages"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="delivery_method",
            field=jutil.modelfields.SafeCharField(
                choices=[("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                db_index=True,
                max_length=1,
                verbose_name="delivery method",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="entry_type",
            field=jutil.modelfields.SafeCharField(
                choices=[
                    ("1", "Deposit"),
                    ("2", "Withdrawal"),
                    ("3", "Deposit Correction"),
                    ("4", "Withdrawal Correction"),
                ],
                db_index=True,
                max_length=1,
                verbose_name="entry type",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="family_code",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=4, verbose_name="family code"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="messages",
            field=jutil.modelfields.SafeTextField(blank=True, default="", verbose_name="messages"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="name",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=64, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="name_source",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[("", "Not Set"), ("A", "From Customer"), ("K", "From Bank Clerk"), ("J", "From Bank System")],
                max_length=1,
                verbose_name="name source",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="receipt_code",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[("", ""), ("E", "Separate"), ("P", "Separate/Paper")],
                db_index=True,
                max_length=1,
                verbose_name="receipt code",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="recipient_account_number",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=32, verbose_name="recipient account number"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="recipient_account_number_changed",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=1, verbose_name="recipient account number changed"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="record_code",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[
                    ("700", "Money Transfer (In/Out)"),
                    ("701", "Recurring Payment (In/Out)"),
                    ("702", "Bill Payment (Out)"),
                    ("703", "Payment Terminal Deposit (In)"),
                    ("704", "Bank Draft (In/Out)"),
                    ("705", "Reference Payments (In)"),
                    ("706", "Payment Service (Out)"),
                    ("710", "Deposit (In)"),
                    ("720", "Withdrawal (Out)"),
                    ("721", "Card Payment (Out)"),
                    ("722", "Check (Out)"),
                    ("730", "Bank Fees (Out)"),
                    ("740", "Interests Charged (Out)"),
                    ("750", "Interests Credited (In)"),
                    ("760", "Loan (Out)"),
                    ("761", "Loan Payment (Out)"),
                    ("770", "Foreign Transfer (In/Out)"),
                    ("780", "Zero Balancing (In/Out)"),
                    ("781", "Sweeping (In/Out)"),
                    ("782", "Topping (In/Out)"),
                ],
                db_index=True,
                max_length=4,
                verbose_name="record type",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="record_description",
            field=jutil.modelfields.SafeCharField(blank=True, default="", max_length=128, verbose_name="record description"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="record_domain",
            field=jutil.modelfields.SafeCharField(
                blank=True,
                choices=[
                    ("PMNT", "Money Transfer (In/Out)"),
                    ("LDAS", "Loan Payment (Out)"),
                    ("CAMT", "Cash Management"),
                    ("ACMT", "Account Management"),
                    ("XTND", "Entended Domain"),
                    ("SECU", "Securities"),
                    ("FORX", "Foreign Exchange"),
                    ("XTND", "Entended Domain"),
                    ("NTAV", "Not Available"),
                ],
                db_index=True,
                max_length=4,
                verbose_name="record domain",
            ),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="remittance_info",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=35, verbose_name="remittance info"),
        ),
        migrations.AlterField(
            model_name="statementrecord",
            name="sub_family_code",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=4, verbose_name="sub family code"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="archive_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=64, verbose_name="archive identifier"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="batch_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, default="", max_length=64, verbose_name="batch message id"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="creditor_account",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=35, verbose_name="creditor account"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="creditor_name",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=128, verbose_name="creditor name"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="currency_code",
            field=jutil.modelfields.SafeCharField(max_length=3, verbose_name="currency code"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="debtor_name",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=128, verbose_name="debtor name"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="end_to_end_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=64, verbose_name="end-to-end identifier"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="ultimate_debtor_name",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=128, verbose_name="ultimate debtor name"),
        ),
        migrations.AlterField(
            model_name="statementrecorddetail",
            name="unstructured_remittance_info",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=2048, verbose_name="unstructured remittance info"),
        ),
        migrations.AlterField(
            model_name="statementrecordremittanceinfo",
            name="additional_info",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=256, verbose_name="additional remittance info"),
        ),
        migrations.AlterField(
            model_name="statementrecordremittanceinfo",
            name="currency_code",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=3, verbose_name="currency code"),
        ),
        migrations.AlterField(
            model_name="statementrecordremittanceinfo",
            name="reference",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=35, verbose_name="reference"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="archive_identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=64, verbose_name="archive identifier"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="bic_code",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=35, verbose_name="BIC"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="iban_account_number",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=35, verbose_name="IBAN"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="identifier",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=35, verbose_name="identifier"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="payer_name_detail",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=70, verbose_name="payer name detail"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="recipient_name_detail",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=70, verbose_name="recipient name detail"),
        ),
        migrations.AlterField(
            model_name="statementrecordsepainfo",
            name="reference",
            field=jutil.modelfields.SafeCharField(blank=True, max_length=35, verbose_name="reference"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="debug_commands",
            field=jutil.modelfields.SafeTextField(blank=True, verbose_name="debug commands"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="environment",
            field=jutil.modelfields.SafeCharField(default="PRODUCTION", max_length=32, verbose_name="environment"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="name",
            field=jutil.modelfields.SafeCharField(max_length=64, verbose_name="name"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="receiver_identifier",
            field=jutil.modelfields.SafeCharField(max_length=32, verbose_name="receiver identifier"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="sender_identifier",
            field=jutil.modelfields.SafeCharField(max_length=32, verbose_name="sender identifier"),
        ),
        migrations.AlterField(
            model_name="wsediconnection",
            name="target_identifier",
            field=jutil.modelfields.SafeCharField(max_length=32, verbose_name="target identifier"),
        ),
        migrations.AlterField(
            model_name="wsedisoapcall",
            name="command",
            field=jutil.modelfields.SafeCharField(blank=True, db_index=True, max_length=64, verbose_name="command"),
        ),
        migrations.AlterField(
            model_name="wsedisoapcall",
            name="error",
            field=jutil.modelfields.SafeTextField(blank=True, verbose_name="error"),
        ),
    ]
