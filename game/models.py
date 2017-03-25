from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    id_player_1 = models.IntegerField(max_length=40, default=0)
    id_player_2 = models.IntegerField(max_length=40, default=0)
    pending_request = models.BooleanField(default=False)
    gesture_1 = models.CharField(max_length=40, default="paper")
    gesture_2 = models.CharField(max_length=40, default="paper")

