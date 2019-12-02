import logging
import os
from copy import copy
from pathlib import Path
from pprint import pprint
from django.conf import settings
from django.core.files import File
from django.core.management import CommandParser
from django.db import transaction
from django.utils import translation
from jacc.models import Account, AccountType
from jbank.helpers import create_statement, create_reference_payment_batch, get_or_create_bank_account
from jbank.files import list_dir_files
from jbank.models import Statement, ReferencePaymentBatch, ReferencePaymentBatchFile, ReferencePaymentRecord, \
    StatementFile, StatementRecord
from jbank.parsers import parse_svm_batches_from_file, parse_tiliote_statements_from_file
from jutil.command import SafeCommand
from django.utils.translation import gettext as _


logger = logging.getLogger(__name__)


class Command(SafeCommand):
    help = 'Re-parses old bank statement .TO (tiliote) files. Used for adding missing fields.'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--file', type=str)

    def do(self, *args, **options):
        logger.info('Re-parsing TO files to update fields')
        qs = StatementFile.objects.all()
        if options['file']:
            qs = qs.filter(file=options['file'])
        for file in qs.order_by('id'):
            assert isinstance(file, StatementFile)
            logger.info('Processing {} BEGIN'.format(file))
            statements = parse_tiliote_statements_from_file(file.full_path)
            for data in statements:
                for e in data['records']:
                    # check missing line_number
                    e2 = StatementRecord.objects.filter(statement__file=file, line_number=0, record_number=e['record_number'], archive_identifier=e['archive_identifier'], record_date=e['record_date'], value_date=e['value_date'], paid_date=e['paid_date'], entry_type=e['entry_type'], record_code=e['record_code'], record_description=e['record_description'], receipt_code=e['receipt_code'], delivery_method=e['delivery_method'], name=e['name'], name_source=e['name_source'], recipient_account_number=e['recipient_account_number'], recipient_account_number_changed=e['recipient_account_number_changed'], remittance_info=e['remittance_info']).first()
                    if e2:
                        e2.line_number = e['line_number']
                        e2.save()
                        logger.info('Updated {} line number to {}'.format(e2, e2.line_number))
            logger.info('Processing {} END'.format(file))
