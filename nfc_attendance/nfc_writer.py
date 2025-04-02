# nfc_writer.py (Write student IDs to NFC cards)
import nfc
from nfc.tag import Tag

def write_student_id(student_id):
    clf = nfc.ContactlessFrontend('usb')  # Adjust for your reader
    if clf:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        if tag.ndef:
            record = nfc.ndef.TextRecord(student_id)
            tag.ndef.records = [record]
            print(f"Wrote student ID {student_id} to NFC tag.")
        clf.close()

write_student_id("STUDENT_123")