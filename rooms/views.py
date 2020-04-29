
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from django_countries import countries
from . import models

"""
from math import ceil
from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", context={"page": rooms},)
    except EmptyPage:
        return redirect("/")
"""


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

"""
def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
"""


class RoomDetail(DetailView):
    """ RoomDetail Definition """
    
    model = models.Room
    

def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    form = {
        "city": city, "s_room_type": room_type, "s_country": country, 
        "price": price, "guests": guests, "bedrooms": bedrooms,
        "beds": beds, "baths": baths,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    choices = {"countries": countries, "room_types": room_types,
               "amenities": amenities, "facilities": facilities}


    return render(request, "rooms/search.html", {**form, **choices})