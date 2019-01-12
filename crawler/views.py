from django.shortcuts import render

# Create your views here.
def landing(request, template_name='crawler/landing.html'):
    return render(request, template_name)
