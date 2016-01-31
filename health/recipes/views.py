from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Recipe


def index(request):
    latest_recipe_list = Recipe.objects.order_by('-datePublished')[:5]
    template = loader.get_template('recipes/index.html')
    context = {
        'latest_recipe_list': latest_recipe_list,
    }
    return HttpResponse(template.render(context, request))