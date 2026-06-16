from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu , Booking
from .serializers import MenuItemSerializer , BookingSerializer
from rest_framework import viewsets






def index(request):
    return render(request , 'restaurant/index.html', {})

class MenuItemView(generics.ListCreateAPIView):

    queryset = Menu.objects.all()

    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
#    permission_classes = [permissions.IsAuthenticated] #    Require the client to be authenticated before accessing any of these endpoints.