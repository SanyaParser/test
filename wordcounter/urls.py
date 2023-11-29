from django.urls import path
from .views import home, load_file, word_count, clear_memory

app_name = 'wordcounter'

urlpatterns = [
    path('', home, name='home'),
    path('load_file/', load_file, name='load_file'),
    path('word_count/', word_count, name='word_count'),
    path('clear_memory/', clear_memory, name='clear_memory'),
]