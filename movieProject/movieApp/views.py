from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import movieForm
from .models import movies

# Create your views here.
def index(request):
    movie= movies.objects.all
    context = {
        'movie_data': movie,
        'head': 'Home',
        'button': 'Add Movies'
    }
    return render(request,'index.html', context)


def details(request,movieId):
    movie = movies.objects.get(id= movieId)
    return render(request,'detail.html',{'movie':movie,'head': 'Details'})


def addMovie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = movies(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(request,'add.html', {'head':'Add Movie'})


def update(request, id):
    movie = movies.objects.get(id=id)
    form = movieForm(request.POST or None, request.FILES, instance= movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'form': form, 'movie': movie, 'head':'update'})


def delete(request,id):
    if request.method== 'POST':
        movie = movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html', {'head': 'delete'})

