from django.views import View 
from django.views.generic import TemplateView 
from pathlib import Path
from random import randint
from django.http import JsonResponse
import json


class AutocorrectBase(TemplateView):
    template_name="autocorrect.html"


class ServeRandom(View):
    def get(self, request, *args, **kwargs):
        
        # define dataset to use
        dataset_path = Path('.').parent / 'dataset' / 'test'
        dataset_file = dataset_path.joinpath('29.json')
        
        # read in all tweets from file
        with dataset_file.open(mode='r') as f:
            contents = f.readlines()

        # pick tweet at random
        tweet_no = randint(0, len(contents))

        # select one at random
        return JsonResponse(json.loads(contents[tweet_no]))
