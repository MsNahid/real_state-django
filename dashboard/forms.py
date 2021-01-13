from django.forms import ModelForm
from realtors.models import Realtor
from listings.models import Listing

#Realtor
class RealtorForm(ModelForm):
    class Meta:
        model = Realtor
        fields = '__all__'


#Listing
class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['realtor', 'title', 'is_published']
