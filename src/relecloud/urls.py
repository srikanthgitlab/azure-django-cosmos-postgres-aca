from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("destinations/", views.destinations, name="destinations"),
    path(
        "destination/<int:pk>",
        views.DestinationDetailView.as_view(),
        name="destination_detail",
    ),
    path("cruise/<int:pk>", views.CruiseDetailView.as_view(), name="cruise_detail"),
    path("info_request", views.InfoRequestCreate.as_view(), name="info_request"),
     #path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('create', views.create_restaurant, name='create_restaurant'),
    path('add', views.add_restaurant, name='add_restaurant'),
    path('review/<int:id>', views.add_review, name='add_review'),
]
