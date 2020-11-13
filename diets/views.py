from django.shortcuts import render
from .models import Diet
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class DietView(APIView):

    def get(self, request):
        diet = Diet.objects.first()
        if not diet:
            return Response({
                'breakfast': '',
                'lunch': '',
                'dinner': ''
            })
        return Response({
            'breakfast': diet.breakfast,
            'lunch': diet.lunch,
            'dinner': diet.dinner
        })
