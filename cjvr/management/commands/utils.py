from random import randint

def generateIntervalle() :
    x = randint(1, 8)
    y = 0
    while x > y :
        y = randint(1, 8)
    intervalle = [x, y]

    return intervalle
