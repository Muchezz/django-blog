from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Mucheru',
        'title' : 'Blog Post 1',
        'content': 'First blog post',
        'date_posted': 'May 14, 2021'
    },
    {
        'author' : 'James',
        'title' : 'Blog Post 2',
        'content': 'Second blog post',
        'date_posted': 'May 15, 2021'
    }
]

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {
        'posts':posts
    } )

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})