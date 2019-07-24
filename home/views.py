from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def bytext(request):
    return render(request,'bytext.html')
