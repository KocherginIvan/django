from django.shortcuts import render

from parserapp.forms import CommentForm
from parserapp.models import Book


# Create your views here.
def main_view(request):
    books = Book.objects.all()
    num = 1
    book_out = []
    # for book in books:
    #     print(book.authors)
    #     auth = [str(author) for author in book.authors.all()]
    #     au = auth[0]
    #     for a in auth:
    #         if a != au:
    #             au += f', {a}'
    #     book.authors = au

    return render(request, 'parserapp/index.html', {'book_out': books})
def work_view(request, id):
    if request.method == 'POST':
        books = Book.objects.all()
        book = books.get(id=id)
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            return render(request, 'parserapp/work.html', {'book': book, 'form': form, 'name': name, 'comment': comment})
        else:
            return render(request, 'parserapp/work.html', {'book': book, 'form': form, 'name': '', 'comment': ''})
    else:
        books = Book.objects.all()
        book = books.get(id=id)
        form = CommentForm()
    return render(request, 'parserapp/work.html', {'book': book, 'form': form, 'name': '', 'comment': ''})