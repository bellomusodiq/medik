from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class Chat(APIView):

    def post(self, request):
        message = request.data.get("message")
        # perform forward feed here

        return Response({"message": "Hang in there, Stay strong chanp."}, 200)


class SymptomsList(APIView):

    def get(self, request):
        symptoms = [
            'headache',
            'itching',
            'vomiting',
            'skin_rash'
        ]
        return Response(symptoms)


class IllnessClassifier(APIView):

    def post(self, request):
        """
        :param request: symptoms: list
        :return: {'illness': str}
        """
        symptoms = request.data
        # run classification model here
        print(symptoms)
        return Response({"illness": "malaria"})
