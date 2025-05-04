from datetime import timezone
import os
from typing import Any, Dict
import uuid

from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db.models import Avg, Count
from requests import RequestException
from requests import RequestException, exceptions
from django.contrib import messages

from . import models

# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, "destinations.html", {"destinations": all_destinations})


class DestinationDetailView(generic.DetailView):
    template_name = "destination_detail.html"
    model = models.Destination

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cruises"] = self.get_object().cruises.all()
        return context


class CruiseDetailView(generic.DetailView):
    template_name = "cruise_detail.html"
    model = models.Cruise


class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = "info_request_create.html"
    model = models.InfoRequest
    fields = ["name", "email", "cruise", "notes"]
    success_url = reverse_lazy("index")
    success_message = "Thank you, %(name)s! We will email you when we have more information about %(cruise)s!"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cruises"] = models.Cruise.objects.all()  # Pass all cruises to the template
        return context



# Create your views here.

# def index(request):
#     print('Request for index page received')
#     restaurants = Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review'))
#     return render(request, 'restaurant_review/index.html', {'restaurants': restaurants })


def details(request, id):
    print('Request for restaurant details page received')
    

    # Get account_url based on environment
    
    image_path = "/" 

    try: 
        restaurant = models.Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review')).get(pk=id)
    except models.Restaurant.DoesNotExist:
        raise Http404("Restaurant doesn't exist")
    return render(request, 'restaurant_review/details.html', {'restaurant': restaurant, 
        'image_path': image_path})


def create_restaurant(request):
    print('Request for add restaurant page received')

    return render(request, 'restaurant_review/create_restaurant.html')

def add_restaurant(request):
    try:
        name = request.POST['restaurant_name']
        street_address = request.POST['street_address']
        description = request.POST['description']
        if (name == "" or description == ""):
            raise RequestException()
    except (KeyError, exceptions.RequestException) as e:
        # Redisplay the restaurant entry form.
        messages.add_message(request, messages.INFO, 'Restaurant not added. Include at least a restaurant name and description.')
        return HttpResponseRedirect(reverse('create_restaurant'))  
    else:
        restaurant = models.Restaurant()
        restaurant.name = name
        restaurant.street_address = street_address
        restaurant.description = description
        models.Restaurant.save(restaurant)

       
                
        return HttpResponseRedirect(reverse('details', args=(restaurant.id,)))

def add_review(request, id):
    try: 
        restaurant = models.Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review')).get(pk=id)
    except models.Restaurant.DoesNotExist:
        raise Http404("Restaurant doesn't exist")

    try:
        user_name = request.POST['user_name']
        rating = request.POST['rating']
        review_text = request.POST['review_text']
        if (user_name == "" or rating == ""):
            raise RequestException()            
    except (KeyError, exceptions.RequestException) as e:
        # Redisplay the details page
        messages.add_message(request, messages.INFO, 'Review not added. Include at least a name and rating for review.')
        return HttpResponseRedirect(reverse('details', args=(id,)))  
    else:

        if 'reviewImage' in request.FILES:
            image_data = request.FILES['reviewImage']
            print("Original image name = " + image_data.name)
            print("File size = " + str(image_data.size))

            if (image_data.size > 2048000):
                messages.add_message(request, messages.INFO, 'Image too big, try again.')
                return HttpResponseRedirect(reverse('details', args=(id,)))  

            # Get account_url based on environment
            
            # Get file name to use in database
            image_name = str(uuid.uuid4()) + ".png"
            
            # Create blob client
            print("\nUploading to Azure Storage as blob:\n\t" + image_name)

            # Upload file
           
        else:
            # No image for review
            image_name=None

        review = models.Review()
        review.restaurant = restaurant
        review.review_date = timezone.now()
        review.user_name = user_name
        review.rating = rating
        review.review_text = review_text
        review.image_name = image_name
        models.Review.save(review)

       
        
    return HttpResponseRedirect(reverse('details', args=(id,)))


