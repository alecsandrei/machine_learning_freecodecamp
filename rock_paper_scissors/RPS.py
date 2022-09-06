# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):

    if prev_play != "":
        opponent_history.append(prev_play)
    counter = len(opponent_history)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if prev_play == "":
        guess = 'P'
    elif counter % 2 == 0 and opponent_history[-1] != opponent_history[-2]:
        guess = ideal_response[prev_play]
    elif counter % 3 == 0:
        guess = ideal_response[ideal_response[prev_play]]
    else:
        guess = ideal_response[prev_play]

    return guess
