
from random import (randint)

diapazonas = int(input("Įveskite spėjamo skaičiaus diapazoną: "))
spejamas_skaicius = randint(1, diapazonas)

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
