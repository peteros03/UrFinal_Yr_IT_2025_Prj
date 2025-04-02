import nfc
from nfc.tag import Tag
from django.core.management.base import BaseCommand
from core.models import Student

def write_nfc_tag(student_id, url):
    try:
        clf = nfc.ContactlessFrontend('usb')
        if clf:
            tag = clf.connect(rdwr={'on-connect': lambda tag: False})
            if tag.ndef:
                record = nfc.ndef.UriRecord(url)
                tag.ndef.records = [record]
                print(f"Successfully wrote URL: {url}")
            clf.close()
    except Exception as e:
        print(f"Error: {str(e)}")

class Command(BaseCommand):
    help = 'Write student URL to NFC card'

    def add_arguments(self, parser):
        parser.add_argument('student_id', type=str, help='Student ID')

    def handle(self, *args, **kwargs):
        student_id = kwargs['student_id']
        try:
            student = Student.objects.get(student_id=student_id)
            url = f"http://localhost:8000{student.card_url}"
            write_nfc_tag(student_id, url)
            self.stdout.write(self.style.SUCCESS(f'Successfully programmed card for {student.name}'))
        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR('Student not found'))