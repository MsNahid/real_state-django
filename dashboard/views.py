from django.shortcuts import render, redirect

from listings.models import Listing
from realtors.models import Realtor
from django.contrib.auth.models import User

from .forms import RealtorForm, ListingForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin'])
def dash(request):

    #Dashboard count card
    properties = Listing.objects.count()
    published = Listing.objects.filter(is_published=True).count()
    not_published = Listing.objects.filter(is_published=False).count()

    #Realtors
    realtors = Realtor.objects.order_by('hire_date')[:5]

    #user
    users = User.objects.filter(is_staff=False)

    #Property
    listings = Listing.objects.order_by('-list_date')

    context = {
        'properties': properties,
        'published': published,
        'not_published': not_published,
        'realtors': realtors,
        'listings': listings,
        'users':users,

    }

    return render(request, 'dashboard/controll.html', context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin'])
def create_realtors(request):

    form = RealtorForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = RealtorForm(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dash')

    context = {
        'form': form,
    }

    return render(request, 'dashboard/create_realtors.html', context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin'])
def update_property(request, pk):

    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ListingForm(request.POST,  request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dash')

    context = {
        'form': form,

    }

    return render(request, 'dashboard/update.html', context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin'])
def delete_property(request, pk):

    listing = Listing.objects.get(id=pk)
    if request.method == 'POST':
        listing.delete()
        print("ok boss")
        return redirect('dashboard:dash')

    context = {
        'listing': listing,

    }
    return render(request, 'dashboard/delete.html', context)


