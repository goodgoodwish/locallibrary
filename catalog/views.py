from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    # practice
    num_o_genres = Genre.objects.filter(name__icontains="o").count()
    num_o_books = Book.objects.filter(title__icontains="o").count()
    num_o_book_list = Book.objects.filter(title__icontains="o")
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        "num_o_genres": num_o_genres,
        "num_o_books": num_o_books,
        "num_o_book_list": num_o_book_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)

