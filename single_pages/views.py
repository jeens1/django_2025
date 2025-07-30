from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,
                  'single_pages/landing.html',
                  context={
                      'name':'홍길동','title':'landing'
                  })

def home(request):
    return render(request, 'home.html')