from django.shortcuts import render

from .models import Shortner
from .forms import ShortenerForm

from django.http import HttpResponse,Http404,HttpResponseRedirect

def home_view(request):
    template = "home.html"

    context = {}

    context['form'] = ShortenerForm()

    if request.method =='GET':
        return render(request,template,context)

    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            shortener_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortener_object.short_url

            long_url = shortener_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request,template,context)

        context['errors'] = used_form.errors

        return render(request,template,context)


def redirect_url_view(request,shortend_part):

    try:
        shortner = Shortner.objects.get(short_url = shortend_part)

        shortner.times_followed += 1
        shortner.save()


        return HttpResponseRedirect(shortner.long_url)


    except:
        raise Http404("Sorry this link is broken")
