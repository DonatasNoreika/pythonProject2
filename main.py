
from random import (randint)

nuo = 1
iki = int(input("Įveskite spėjamo skaičiaus diapazoną: "))
diapazonas_nuo = nuo
diapazonas_iki = iki
spejamas_skaicius = randint(nuo, iki)

skaitiklis = 0

while True:
    print(f"Diapazonas: nuo {diapazonas_nuo} iki {diapazonas_iki}")
    spejimas = int(input("Spėkite skaičių: "))
    if spejimas >= diapazonas_iki or spejimas <= diapazonas_nuo:
        print("Pasirinkote skaičių už diapazono")
        continue
    skaitiklis += 1
    print("Spėjimai", skaitiklis)

    if spejimas == spejamas_skaicius:
        print(f'Skaičius {spejamas_skaicius} atspėtas!')
        print(f"Spėjimų skaičius: {skaitiklis}")
        break
    if spejimas > spejamas_skaicius:
        print("Mažiau")
        diapazonas_iki = spejimas
    if spejimas < spejamas_skaicius:
        print("Daugiau")
        diapazonas_nuo = spejimas
