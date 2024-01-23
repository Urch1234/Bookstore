# update_book_ids.py

from django.core.management.base import BaseCommand
from books.models import Book  # Replace 'app_name' with your app's name
import uuid


class Command(BaseCommand):
    def handle(self, *args, **options):
        for book in Book.objects.all():
            book.id = uuid.uuid4()
            book.save()
