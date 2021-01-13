from django.contrib import admin

from .models import Listing, SearchResult

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published', 'price', 'realtor')
    search_fields = ('title','descriptions', 'address', 'city', 'state', 'zipcode')
    list_per_page = 25

class SearchResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'search_key', 'search_count', 'list_date')
    list_display_links = ('id', 'search_key')
    list_per_page = 10


    
admin.site.register(Listing, ListingAdmin)
admin.site.register(SearchResult, SearchResultAdmin)
