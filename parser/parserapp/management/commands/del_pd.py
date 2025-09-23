from django.core.management.base import BaseCommand, CommandError
from parserapp.models import Author, Book, Comment
from parser_author import create_soup, parse_soup
import pprint
class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.all()
        # books_auth = Book.objects.all().prefetch_related('authors')
        # for book in books_auth:
        #     print(book.authors.all())
        # print(Book.objects.values('id').first()['id'])
        # print(Book.objects.filter(authors__name='Олег Сапфир'))
        # Book.objects.all().delete()
        # Author.objects.all().delete()
        Comment.objects.all().delete()
        num = 0
        book_out = []
        # for book in books:
        #     print(book.img_href)

            # auth = [str(author) for author in book.authors.all()]
            # au = auth[0]
            # for a in auth:
            #     if a != au:
            #         au += f', {a}'
            # book.authors = au

        # for book in books:
        #     auth = [str(author) for author in book.authors.all()]
        #     authors = ''
        #     for a in auth:
        #         authors += f'{a} '
        #     book_out.append([num, book.title, authors, book.content, book.href])
        # # for titles, authors, contents, hrefs in book_out.values():
        # #     print(contents)
        # print(book_out[0])


        # new_book = Book.objects.create(title=f'{books_out[book]['Название книги']}',
        #                     content=f'{books_out[book]['Краткое содержание']}', href=f'{books_out[book]['Ссылка на книгу']}')
        # for author in books_out[book]['Автор'].split(', '):
        #     if Author.objects.filter(name= author).count() == 0:
        #         new_author = Author.objects.create(name=f'{author}')
        #         new_book.authors.add(new_author)
        #     else:
        #         new_author = Author.objects.filter(name=f'{author}').first()
        #         new_book.authors.add(new_author)
        # new_book.save()



