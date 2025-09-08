from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin

from parserapp.forms import CommentForm
from parserapp.models import Book, Comment
from userapp.models import UserAuthor

# Create your views here.
class BookListView(ListView):
    paginate_by = 12
    model = Book
    queryset  = Book.objects.prefetch_related('authors')
    template_name = 'parserapp/index.html'

class WorkDetail(DetailView):
    model = Book
    template_name = 'parserapp/work.html'
    queryset = Book.objects.prefetch_related('authors', 'comments')

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'parserapp/comment.html'
    form_class = CommentForm
    def form_valid(self, form):
        Book.objects.get(id=self.request.path.split('/')[-1]).comments.create(name=self.request.user,
                                             comment=f'{self.request.POST['comment']}')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['book'] =Book.objects.prefetch_related('authors').get(id = self.request.path.split('/')[-1])
        return context
    def get_success_url(self):
        return reverse(viewname='parserapp:work', kwargs={'pk': self.request.path.split('/')[-1]})
