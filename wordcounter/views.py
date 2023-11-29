from django.shortcuts import render, redirect
from .forms import FileUploadForm, WordCountForm
from .models import LoadedFile
import re

def home(request):
    loaded_files = LoadedFile.objects.all()
    return render(request, 'wordcounter/home.html', {'loaded_files': loaded_files})

def load_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            content = file.read().decode('utf-8')
            words = re.findall(r'\b[A-Za-z]+\b', content)
            for word in words:
                LoadedFile.objects.create(file=file, word=word)
            return redirect('wordcounter:home')
    else:
        form = FileUploadForm()
    return render(request, 'wordcounter/load_file.html', {'form': form})

def word_count(request):
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            count = LoadedFile.objects.filter(word=word).count()
            return render(request, 'wordcounter/word_count.html', {'count': count, 'word': word})
    else:
        form = WordCountForm()
    return render(request, 'wordcounter/word_count_form.html', {'form': form})

def clear_memory(request):
    LoadedFile.objects.all().delete()
    return redirect('wordcounter:home')