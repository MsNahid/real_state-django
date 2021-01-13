from django.shortcuts import render

# Create your views here.

def profile(request, realtors_id):

    context = {

    }

    return render(request, 'realtors/profile.html')
