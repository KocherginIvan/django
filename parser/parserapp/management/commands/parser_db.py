from django.core.management.base import BaseCommand, CommandError
from parserapp.models import Author, Book
from parser_author import create_soup, parse_soup

class Command(BaseCommand):

    def handle(self, *args, **options):
        soup = create_soup('https://author.today')
        books_out = parse_soup(soup)
        Book.objects.all().delete()
        Author.objects.all().delete()
        for book in books_out:
            new_book = Book.objects.create(title=f'{books_out[book]['Название книги']}',
                                content=f'{books_out[book]['Краткое содержание']}', href=f'{books_out[book]['Ссылка на книгу']}',img_href= f'{books_out[book]['Ссылка на обложку']}')
            for author in books_out[book]['Автор'].split(', '):
                if Author.objects.filter(name= author).count() == 0:
                    new_author = Author.objects.create(name=f'{author}')
                    new_book.authors.add(new_author)
                else:
                    new_author = Author.objects.filter(name=f'{author}').first()
                    new_book.authors.add(new_author)
            new_book.save()



