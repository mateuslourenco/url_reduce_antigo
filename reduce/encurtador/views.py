from django.http import HttpResponse
from django.shortcuts import render, redirect

from reduce.encurtador.models import UrlRedirect


def redirecionar(request, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect.destino)
