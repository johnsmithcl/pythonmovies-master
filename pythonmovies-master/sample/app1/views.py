from django.shortcuts import render,redirect
from django.http import HttpResponse
from  .models import Movie
from .forms import Movieform
# Create your views here.

def movie(request):
    movie=Movie.objects.all()
    c={'list':movie}
    return render(request,'index.html',c)

def detail(request,movie_id):
    m=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':m})


def add(request):
    if request.method=='POST':
        n=request.POST.get('name')
        d = request.POST.get('desc')
        y = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=n,desc=d,year=y,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
