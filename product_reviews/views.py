from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import ReviewSerializer
from . models import Review
from products import serializers

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        products = Review.objects.all()
        serializer = ReviewSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    product = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    