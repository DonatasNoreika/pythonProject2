

def tikrinti_spejima(spejimas, spejamas_skaicius):
    if spejimas > spejamas_skaicius:
        print("Mažiau")
        # diapazonas_iki = spejimas
    if spejimas < spejamas_skaicius:
        print("Daugiau")
        # diapazonas_nuo = spejimas
    if spejimas == spejamas_skaicius:
        return True
    return False
