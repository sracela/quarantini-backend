from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'$', views.CardList.as_view()),
    url(r'(?P<pk>[0-9]+)$', views.CardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
