from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu , Booking
from .serializers import MenuItemSerializer , BookingSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response






@api_view(['GET'])
@permission_classes([IsAuthenticated])

def msg(request):
    return Response({"message": "This view is protected"})

def index(request):
    return render(request , 'restaurant/index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated] #    Require the client to be authenticated before accessing any of these endpoints.