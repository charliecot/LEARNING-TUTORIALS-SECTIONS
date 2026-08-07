from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person,AssertModel
from .serializer import  PersonSerializer,AssertSerializer
from rest_framework import status
# Create your views here.



@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        try:
            query_set= AssertModel.objects.all()
            serializer=AssertSerializer(query_set,many=True)
            data=serializer.data
            print(data[0]['persons'][0])
            return Response({
                'data':data,
                'message':'data collected safely',
            },status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'status':False,
                'message':'data not properly collected',
            }, status=status.HTTP_400_BAD_REQUEST)
            




