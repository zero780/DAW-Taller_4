from django.urls import path

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^carros/$',CarrosViewSet.as_view(), name ='carros'),
    url(r'^carros/(?P<pk>[0-9]+)/$', CarroDetail.as_view()),
    # path('snippets/', SnippetDetailView.as_view()),
    #path('', index1, name='index1'),
]