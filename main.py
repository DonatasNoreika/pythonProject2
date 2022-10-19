
from random import (randint)

spejamas_skaicius = randint(1, 100)

while True:
    spejimas = int(input("Spėkite skaičių: "))

    if spejimas == spejamas_skaicius:
        print(f'Skaičius {spejamas_skaicius} atspėtas!')
        break