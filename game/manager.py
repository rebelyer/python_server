from game.models import Game
from django.db import models

class GameManager(models.Manager):
    def create_game(self, player_id, gesture):
        game = Game.objects.filter(pending_request=True).last()
        if (game is None):
            return Game.objects.create(id_player_1=player_id,gesture_1=gesture, pending_request=True)
        game.id_player_2 = player_id
        game.gesture_2 = gesture
        game.save()
        return game
