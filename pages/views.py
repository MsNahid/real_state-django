from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing, SearchResult
from realtors.models import Realtor
from listings.choices import *

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    unPublished_listings = Listing.objects.order_by('-list_date').filter(is_published=False)[:3]

    #Popular Searched
    popular_keyword = SearchResult.objects.filter(search_key__exact='keywords').order_by('-search_count')
    popular_city = SearchResult.objects.filter(search_key__exact='city').order_by('-search_count')
    popular_bedroom = SearchResult.objects.filter(search_key__exact='bedrooms').order_by('-search_count')
    popular_price = SearchResult.objects.filter(search_key__exact='price').order_by('-search_count')

    context = {
        'popular_keyword': popular_keyword,
        'popular_city': popular_city,
        'popular_bedroom': popular_bedroom,
        'popular_price': popular_price,
        'unPublished_listings': unPublished_listings,
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,

    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    realtors_mvp = Realtor.objects.all().filter(is_mvp=True)

    context ={
        'realtors':realtors,
        'realtors_mvp':realtors_mvp
    }
    return render(request, 'pages/about.html', context)
