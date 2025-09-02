from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from parserapp.forms import CommentForm
from parserapp.models import Book, Comment


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'parserapp/index.html'

class WorkDetail(DetailView):
    model = Book
    template_name = 'parserapp/work.html'

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'parserapp/comment.html'
    form_class = CommentForm
    def form_valid(self, form):
        print(form.cleaned_data)
        new_comment = Comment.objects.create(name=f'{self.request.POST['name']}',
                                             comment=f'{self.request.POST['comment']}')
        book = Book.objects.get(id=self.request.path.split('/')[-1])
        book.comments.add(new_comment)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['book'] =Book.objects.get(id = self.request.path.split('/')[-1])
        return context
    def get_success_url(self):
        return reverse(viewname='parserapp:work', kwargs={'pk': self.request.path.split('/')[-1]})
