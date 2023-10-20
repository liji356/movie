from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import MovieList
from.forms import MovieForm

def index(request):
    movie=MovieList.objects.all()
    context={
        'movie_list':movie}
    return render(request,'index.html',context)


    #ADD mOVIE#

def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        Year=request.POST.get('Year',)
        image=request.FILES['image',]
        movie=MovieList(name=name,desc=desc,Year=Year,image=image)
        movie.save()
    return render(request,'add.html')

#UPDATE 
def update(request,id):
    movie=MovieList.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,"movie":movie})
#DElete
def delete(request,id):
    if request.method == "POST":
        movie=MovieList.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")








def detalis(request,movie_id):
    movie=MovieList.objects.get(id=movie_id)
    return render(request,'detalis.html',{'movie':movie})
# Create your views here.
