from django.shortcuts import render

# Create your views here.

def data_render(request):
    data ="imagination of data from database goes from backend to front end"
    d ={'app':data}
    return render(request, 'data_render.html',context=d)
