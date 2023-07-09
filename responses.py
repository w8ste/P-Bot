import sys
from itertools import cycle

from PyDictionary import PyDictionary

p_array = [sys.maxsize]
dictionary = PyDictionary()


# list to handle turns
players = ["player0", "player1"]
myIterator = cycle(range(2))


def turn() -> str:
    players[myIterator.__next__()]
    return players[myIterator.__next__()]


def handle_response(massage) -> str:
    if massage[0] == '!':
        massage = massage[1:]
        p_massage = massage.lower()
        if p_massage == 'obi':
            return 'Hello there! \n'
        elif p_massage[0] == 'p':
            if dictionary.meaning(massage) is None:
                return f'{p_massage} is not a word. Now it is {players[myIterator.__next__()]}\'s turn'
            elif p_massage in p_array:
                return f'{p_massage} was mentioned already. Now it is {players[myIterator.__next__()]}\'s turn'
            else:
                p_array.append(p_massage)
                return f'Good Job, {p_massage} is a new word. Now it is {players[myIterator.__next__()]}\'s turn'
    return ""
