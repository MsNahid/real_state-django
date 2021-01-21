from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Listing, SearchResult
from .choices import *
from django.contrib.auth.decorators import login_required

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { 
        'listings': page_obj,

    }
    return render(request, 'listings/listings.html', context)

@login_required(login_url="accounts:login")
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    #KeyWords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # print(type(keywords))
            # print(keywords)
            queryset_list = queryset_list.filter(descriptions__icontains=keywords)
            keyobj = SearchResult.objects.filter(search_key='keywords', search_value=keywords).first()
            if keyobj:
                keyobj.search_count = keyobj.search_count + 1
                keyobj.save()
            else:
                SearchResult.objects.create(search_key='keywords', search_value=keywords)
    # popular_keyword = SearchResult.objects.filter(search_key__exact='keywords').order_by('-search_count')[0]
    # # if popular_keyword:
    # #     for pop in popular_keyword:
    # #         print(pop.search_value)
    # if popular_keyword:
    #     print(popular_keyword.search_count)
    # else:
    #     print("Not Found")
    #City search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            keyobj = SearchResult.objects.filter(search_key='city', search_value=city).first()
            if keyobj:
                keyobj.search_count = keyobj.search_count + 1
                keyobj.save()
            else:
                SearchResult.objects.create(search_key='city', search_value=city)
        
    #state search
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            keyobj = SearchResult.objects.filter(search_key='state', search_value=state).first()
            if keyobj:
                keyobj.search_count = keyobj.search_count + 1
                keyobj.save()
            else:
                SearchResult.objects.create(search_key='state', search_value=state)

    #bedrooms search
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            keyobj = SearchResult.objects.filter(search_key='bedrooms', search_value=bedrooms).first()
            if keyobj:
                keyobj.search_count = keyobj.search_count + 1
                keyobj.save()
            else:
                SearchResult.objects.create(search_key='bedrooms', search_value=bedrooms)
    
     #price search
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            keyobj = SearchResult.objects.filter(search_key='price', search_value=price).first()
            if keyobj:
                keyobj.search_count = keyobj.search_count + 1
                keyobj.save()
            else:
                SearchResult.objects.create(search_key='price', search_value=price)
                
    context = {
        'listings': queryset_list,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'values': request.GET
        #Preserving Forms

    }
    return render(request, 'listings/search.html', context)

