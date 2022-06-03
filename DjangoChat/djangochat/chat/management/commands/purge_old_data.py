from django.core.management.base import BaseCommand, CommandError
from chat.models import Message
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 1 minute'

    def handle(self, *args, **options):
        time_threshold = datetime.now() - timedelta(minutes=1)
        Message.objects.filter(date__lt=time_threshold).delete()
        self.stdout.write('Delete objects older than 1 minute')        