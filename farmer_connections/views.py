from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Farmer_WH_Owner_Connection, Farmer_Buyer_Connection
from .serializers import FarmerConnectionsSerializer, FarmerBuyerConnectionsSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def Farmer_WH_Owner_Connection_View(request):
    if request.method == 'GET': # user requesting data 
        snippets = Farmer_WH_Owner_Connection.objects.all()
        serializer = FarmerConnectionsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = FarmerConnectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def Farmer_Buyer_Connection_View(request):
    
    if request.method == 'GET': # user requesting data 
        snippets = Farmer_Buyer_Connection.objects.all()
        serializer = FarmerBuyerConnectionsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # user posting data
        serializer = FarmerBuyerConnectionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
