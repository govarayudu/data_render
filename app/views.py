from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'Govardhan','age':25}
    return render(request,'data_render.html',context=d)