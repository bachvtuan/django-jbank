#pylint: disable=too-many-branches
import logging
import os
from pprint import pprint
from django.core.files import File
from django.core.management.base import CommandParser
from django.db import transaction
from jbank.helpers import create_statement, get_or_create_bank_account
from jbank.files import list_dir_files
from jbank.models import Statement, StatementFile
from jbank.parsers import parse_tiliote_statements_from_file
from jutil.command import SafeCommand


logger = logging.getLogger(__name__)


class Command(SafeCommand):
    help = 'Parses bank account statement .TO (tiliote) files'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('path', type=str)
        parser.add_argument('--verbose', action='store_true')
        parser.add_argument('--test', action='store_true')
        parser.add_argument('--delete-old', action='store_true')
        parser.add_argument('--auto-create-accounts', action='store_true')
        parser.add_argument('--resolve-original-filenames', action='store_true')
        parser.add_argument('--tag', type=str, default='')

    def do(self, *args, **options):
        files = list_dir_files(options['path'])
        for filename in files:
            plain_filename = os.path.basename(filename)

            if options['resolve_original_filenames']:
                found = StatementFile.objects.filter(statement__name=plain_filename).first()
                if found and not found.original_filename:
                    assert isinstance(found, StatementFile)
                    found.original_filename = filename
                    found.save(update_fields=['original_filename'])
                    logger.info('Original TO statement filename of %s resolved to %s', found, filename)

            if options['delete_old']:
                Statement.objects.filter(name=plain_filename).delete()

            if options['test']:
                statements = parse_tiliote_statements_from_file(filename)
                pprint(statements)
                continue

            if not Statement.objects.filter(name=plain_filename).first():
                print('Importing statement file {}'.format(filename))

                statements = parse_tiliote_statements_from_file(filename)
                if options['verbose']:
                    pprint(statements)

                with transaction.atomic():
                    if not Statement.objects.filter(name=plain_filename).first():
                        file = StatementFile(original_filename=filename, tag=options['tag'])
                        file.save()
                        with open(filename, 'rb') as fp:
                            file.file.save(plain_filename, File(fp))
                        for data in statements:
                            if options['auto_create_accounts']:
                                account_number = data.get('header', {}).get('account_number')
                                if account_number:
                                    get_or_create_bank_account(account_number)

                            create_statement(data, name=plain_filename, file=file)
            else:
                print('Skipping statement file {}'.format(filename))
