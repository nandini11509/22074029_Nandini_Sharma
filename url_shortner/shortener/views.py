from django.shortcuts import render,redirect
from .models import UrlShortener
from .utils import generate_short_code
from django.http import Http404
def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_code = generate_short_code()
        short_url = request.build_absolute_uri('/') + short_code
        UrlShortener.objects.create(long_url=long_url, short_code=short_code)
        return render(request, 'shortener/shortened_url.html', {'short_url': short_url})
    return render(request, 'shortener/shorten_url.html')


def redirect_to_original_url(request, short_code):
    try:
        url_entry = UrlShortener.objects.get(short_code=short_code)
        return redirect(url_entry.long_url)
    except UrlShortener.DoesNotExist:
        raise Http404("Short URL does not exist")
    
# shortener/views.py
def url_list(request):
    urls = UrlShortener.objects.all()
    return render(request, 'shortener/url_list.html', {'urls': urls})


