from django.conf.urls import include, url
from game import views

app_name = 'game'

urlpatterns = [
    url(r'player_a/(?P<gesture>.+)/$', views.play_a),
    url(r'player_b/(?P<gesture>.+)/$', views.play_b),
    url(r'(?P<player_id>.+)/(?P<gesture>.+)/$', views.play),
]
