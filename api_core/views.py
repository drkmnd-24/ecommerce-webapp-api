from api_core.serializers import *

from account.models import Customer, Address

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from rest_framework import status


class CustomerView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerViewLists(APIView):
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk__id=pk)
        except:
            return Response({'error': 'User does not exists'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomerSerializer(customer.data, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressView(APIView):
    def get(self, request):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AddressDetail(APIView):
    def get(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except:
            return Response({'error': 'address does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializer(address, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        address = Address.objects.get(pk=pk)
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViews(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            queryset = Category.objects.get(pk=pk)
        except:
            return Response({'error': 'category does not exist'})

        serializer = CategorySerializer(queryset, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        queryset = Category.objects.get(pk=pk)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
