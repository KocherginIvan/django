from django.urls import path
from parserapp import views
app_name = 'parserapp'
urlpatterns = [
    path('', views.main_view, name= 'index'),
    path('work/<int:id>', views.work_view, name= 'work'),
]