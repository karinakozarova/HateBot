from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView

from django.http import HttpResponse

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            # get sound from request
            tweet = request.GET.get('tweet')
            print("Tweet is ", tweet)
            vectorizeTweet = PredictorConfig.vectorizer.transform([tweet])
            
            prediction = PredictorConfig.regressor.predict(vectorizeTweet)[0]
            
            response = {'IsHateSpeech': bool(prediction)}
            print(response)
            
            return JsonResponse(response)