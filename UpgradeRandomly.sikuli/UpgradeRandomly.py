# start Time Clickers

from time import sleep
from random import randint

switchApp("TimeClickers")

letters = ['a','s','d','f','g']

for i in range(60):
    letter = letters[randint(0,4)]
    type(letter)
    sleep(.5 + .03*i)