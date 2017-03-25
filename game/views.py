from django.shortcuts import render
import json
from django.http import HttpResponse
import urllib
import unicodedata
import time
from game.models import Game
from game.manager import GameManager
# Create your views here.


def play(request, player_id, gesture):
    game = GameManager().create_game(player_id,gesture)
    if (game.pending_request == True and (game.id_player_2 == 0)):
        for i in list(range(4)):
            if (not game.id_player_2 == 0):
                break
            else:
                time.sleep(1)
    game = Game.objects.last()
    if ((game.gesture_1 == "rock" and game.gesture_2 == "paper") or (game.gesture_1 == "scisors" and game.gesture_2 == "rock" ) or (game.gesture_1 == "paper" and game.gesture_2 == "scisors")):
        winer = game.id_player_2
    elif (game.gesture_1 == game.gesture_2):
        winer = "tie"
    else:
        winer = game.id_player_1
    Game.objects.all().update(pending_request=False)
    return HttpResponse(json.dumps({"winner": winer}), content_type="application/json")
