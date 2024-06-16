from django.core.management.base import BaseCommand
from books.models import Books
import faker

class Command(BaseCommand):
    help = 'Insert 100 books into the database'

    def handle(self, *args, **kwargs):
        fake = faker.Faker()

        books = []
        for _ in range(10000):
            book = Books(
                title=fake.sentence(nb_words=5),
                author=fake.name(),
                description=fake.text()
            )
            books.append(book)
        
        Books.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS('Successfully inserted 100000 books'))
