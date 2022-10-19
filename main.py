
from random import (randint)

spejamas_skaicius = randint(1, 100)

skaitiklis = 0

while True:
    spejimas = int(input("Spėkite skaičių: "))
    skaitiklis += 1

    if spejimas == spejamas_skaicius:
        print(f'Skaičius {spejamas_skaicius} atspėtas!')
        print(f"Spėjimų skaičius: {skaitiklis}")
        break
    if spejimas > spejamas_skaicius:
        print("Mažiau")
    if spejimas < spejamas_skaicius:
        print("Daugiau")
