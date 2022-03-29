from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def error404(request, exception):

    template = loader.get_template("404.html")
    return HttpResponse(template.render())


def error500(request):

    template = loader.get_template("500.html")
    return HttpResponse(template.render())
