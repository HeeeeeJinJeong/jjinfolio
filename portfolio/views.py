from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')


def project_mono(request):
    return render(request, 'portfolio/project_mono.html')

def project_pystagram(request):
    return render(request, 'portfolio/project_pystagram.html')

def project_jjinmall(request):
    return render(request, 'portfolio/project_jjinmall.html')