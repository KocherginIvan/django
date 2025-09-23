from django.urls import path
from parserapp import views
app_name = 'parserapp'
urlpatterns = [
    path('', views.BookListView.as_view(), name= 'index'),
    path('work/<int:pk>', views.WorkDetail.as_view(), name= 'work'),
    path('comment/<int:id>', views.CommentCreateView.as_view(), name= 'comment'),
]