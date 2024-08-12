from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view

from .decorators.db_router import using_db
from .models import *
from .serializers.item_serializer import ItemSerializer


@extend_schema(
    request=ItemSerializer
)
@api_view(['POST'])
@require_http_methods("POST")
@using_db("write_db")
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        item = serializer.save()
        return HttpResponse(item, status=status.HTTP_201_CREATED)
    return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@using_db("read_db")
@require_http_methods("GET")
def get_item(request, item_id):
    return HttpResponse(get_object_or_404(Item, id=item_id))
