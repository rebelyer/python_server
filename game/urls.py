from django.conf.urls import include, url
from game import views

app_name = 'game'

urlpatterns = [
    url(r'(?P<player_id>.+)/(?P<gesture>.+)/$', views.play),
]
