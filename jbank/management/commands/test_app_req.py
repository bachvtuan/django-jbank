import logging
import os
from decimal import Decimal

from django.conf import settings
from django.core.management import CommandParser
from jacc.models import AccountType, Account
from jutil.command import SafeCommand
from jutil.format import format_xml_bytes

from jbank.helpers import make_msg_id, validate_xml
from jbank.models import Payout, WsEdiConnection
import jbank


logger = logging.getLogger(__name__)


class Command(SafeCommand):
    help = 'Makes test application request'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--ws', type=int, default=1)
        parser.add_argument('--xsd', type=str)
        parser.add_argument('--command', type=str, default='DownloadFileList')
        parser.add_argument('--file', type=str)

    def do(self, *args, **options):
        ws = WsEdiConnection.objects.get(id=options['ws'])
        if options['file']:
            content = open(options['file'], 'rb').read()
        else:
            content = ws.get_application_request(options['command']).encode()
        print('------------------------------------------------- Application request')
        print(format_xml_bytes(content).decode())
        if options['xsd']:
            validate_xml(content, options['xsd'])
        print('------------------------------------------------- Signed request')
        print(ws.sign_application_request(content.decode()))
