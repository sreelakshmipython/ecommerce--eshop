from django.contrib import messages
from django.shortcuts import render
from eshopapp.models import Product
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query)| Q(description__contains=query))

    if not query or query == "":
        message=messages.error(request,"search not found")
        return render(request,'search.html',{'messages':message})
    return render(request, 'search.html', {'query': query, 'products': products})

