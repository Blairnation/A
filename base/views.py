from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Advocate, Company
from .serializer import AdvocateSerializer, CompanySerializer
from django.db.models import Q
from rest_framework.request import Request
import requests
import os
# from dotenv import load_dotenv
# load_dotenv()

# TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
# print('TWITTER_API_KEY: ', TWITTER_API_KEY)
TWITTER_API_KEY ='AAAAAAAAAAAAAAAAAAAAAN1iqgEAAAAAljDVAs7i29pwBE6O2HPk%2FDCcqSg%3Do3YCYdkcsbgmsH8G3VaGmzGGVsfJSjhlOLE1NIuNGqIEfKjvBm'
# Create your views here.
@api_view(['GET', 'POST'])
def endpoints(request):
  
  data = ['advocates/','advocate-list/', 'advocates/:username', 'companies/']
  return Response(data)


class AdvocateAPIView(APIView):
  serializer_class = AdvocateSerializer

  def get_queryset(self):
    return Advocate.objects.all()
  
  def get(self,request, *args, **kwargs):
    try:
       query= request.query_params['query']
       if query != None:
         advocate = Advocate.objects.get(username__icontains=query)
         serializer = AdvocateSerializer(advocate, many=False)
    except:
      advocate = self.get_queryset()
      serializer = AdvocateSerializer(advocate, many=True)

    return Response(serializer.data)      



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def advocates_list(request):
  if request.method == "GET":
      query = request.GET.get('query')

      if query is None:
        query = ''  

      advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
      context = {'request': request}
      serializer = AdvocateSerializer(advocates, many=True,  context=context)
      return Response(serializer.data)
  
  if request.method == "POST":
    
    advocate = Advocate.objects.create(username=request.data['username'],
                            bio=request.data['bio']
                            )
    context = {'request': request}
    serializer = AdvocateSerializer(advocate, many=False, context=context)
    return Response(serializer.data)
    

# @api_view(['GET', 'PUT', "DELETE"])
# def advocate_details(request, username):
#   advocate = Advocate.objects.get(username=username)

#   if request.method == 'GET':  
#     serializer = AdvocateSerializer(advocate, many=False)
#     return Response(serializer.data)
  
#   if request.method == "PUT":
#     advocate.username = request.data['username']
#     advocate.bio = request.data['bio']

#     advocate.save()

#     serializer = AdvocateSerializer(advocate, many=False)
#     return Response(serializer.data)
  
#   if request.method == "DELETE":
#      advocate.delete()
#      return Response('User was deleted')


class AdvocateDetails(APIView):
  serializer_class = AdvocateSerializer

  def get_object(self, username):
    try:
      return Advocate.objects.get(username=username)
    except Advocate.DoesNotExist:
      pass
      

  def get(self, request, username):
    url = 'https://api.twitter.com/2/users/me'
    header = {'Authorization':'Bearer ' + TWITTER_API_KEY}

    response = requests.get(url, headers=header).json()
    print(response)
    

    advocate = self.get_object(username)
    context = {'request': request}
    serializer = AdvocateSerializer(advocate, many=False, context=context)
    return Response(serializer.data)
  
  def put(self, request, username):
    advocate = self.get_object(username)

    advocate.username = request.data['username']
    advocate.bio = request.data['bio']
    advocate.save()

    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def patch(self, request, username):
    advocate = self.get_object(username)

    advocate.username = request.data.get('username', advocate.username)
    advocate.bio = request.data('bio', advocate.bio)
    advocate.save()

    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def delete(self, request, username):
    advocate = self.get_object(username)

    advocate.delete()
    return Response('Item Was Deleted')

@api_view(['GET'])
def companies_list(request):
  companies = Company.objects.all()
  serializer = CompanySerializer(companies, many=True)
  return Response(serializer.data)

