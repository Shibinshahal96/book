from django.shortcuts import render , get_object_or_404

# Create your views here.
from .models import book

def booklist(request):
    books = book.objects.all()
    
    return render(request, 'MyApp/booklist.html', {'books': books})

def bookcreate(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        publisher = request.POST.get('publisher')
        pubdate = request.POST.get('pubdate')
        
        book.objects.create(title=title, author=author, price=price, publisher=publisher, pubdate=pubdate)
        return redirect("booklist")
    return render(request, 'MyApp/books_forms.html')

