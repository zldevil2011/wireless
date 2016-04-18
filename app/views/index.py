from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(15*60)
def index(request):
	return render(request, "index.html", {});
# Create your views here.
