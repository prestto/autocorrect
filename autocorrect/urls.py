from django.urls import path
from autocorrect.views import AutocorrectBase, ServeRandom

urlpatterns = [
    path('', AutocorrectBase.as_view(),name='autocorrect'),
    path('serve-random', ServeRandom.as_view(),name='serve-random'),
    
]
