from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')

def mission(request):
    return render(request,'Mission Statement.html')

def vision(request):
    return render(request, 'Our Vision.html')

