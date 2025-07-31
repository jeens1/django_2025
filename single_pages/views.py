from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,
                  'single_pages/landing.html',
                  context={
                      'name':'홍길동','title':'landing'
                  })

def aboutme(request):
    return render(request,
                  'single_pages/aboutme.html',
                  context={

                  })