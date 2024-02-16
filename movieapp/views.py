from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import MovieForm

# Create your views here.
def index(request):
    movie1=movie.objects.all()
    context={
        'movie_list':movie1
    }
    return render(request,"index.html",context)


def detail(request,movie_id):
    movies=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movies})

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year= request.POST.get('year')
        img=request.FILES['img']
        mov=movie(name=name,desc=desc,year=year,img=img)
        mov.save()

    return render(request,"add.html")

def update(request,id):
    movi=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movi})

def delete(request,id):
    if request.method=="POST":
        movii=movie.objects.get(id=id)
        movii.delete()
        return redirect('/')
    return render(request,"delete.html")

