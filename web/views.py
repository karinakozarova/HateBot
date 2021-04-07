from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from predictor.apps import PredictorConfig

@csrf_exempt 
def homePageView(request):
    if request.method == 'GET':
        return render(request, 'classify.html', {'is_processed': False})
    else: 
        tweet = request.POST.get('tweet')
        print("Tweet is ", tweet)

        vectorizeTweet = PredictorConfig.vectorizer.transform([tweet])
        prediction = PredictorConfig.regressor.predict(vectorizeTweet)[0]
        response = {'IsHateSpeech': bool(prediction)}

        context = {"is_hate": bool(prediction), 'is_processed': True}
        return render(request, 'classify.html', context)