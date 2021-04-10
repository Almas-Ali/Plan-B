from django.shortcuts import render
import config
from execution.models import Profile

# Create your views here.

context = {
    'config': config,
}


def index(request):
    return render(request, 'execution/index.html', context)


def fillup(request):
    return render(request, 'execution/fillup.html', context)


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        search = search.lower().strip()
        u = Profile.objects.filter(name__icontains=search)
        print(u)
        context['results'] = u
    return render(request, 'execution/search.html', context)


def profile(request):
    return render(request, 'execution/profile.html', context)
