# Python-laskin
# Toivo Muukkonen
# Versiohistoria
# 20.5.2025 8.45: Muutettu jatkumoita ja lisätty time-kirjasto, jota hyödynnetään jatkumossa. Odotetaan sekunti, ennen kuin laskin suljetaan.
# 19.5.2025 16.00: Hienosäätöä. Muutos jatkumoihin.
# 18.5.2025 19.30: Laskin tehty, ensimmäinen versio

import time

print("Tervetuloa laskemaan. Muistathan kirjoittaa desimaaliluvut pisteellä. Vastaa vain numeroilla, kun pyydetään lukua.")

while True:
    laskutapa = input("Valitse laskutapa (summa/erotus/tulo/osamaara/peruuta)\n")

    if laskutapa == "summa":
        luku1 = float(input("Mihin lukuun lisataan?\n"))
        luku2 = float(input("Mitä lisataan lukuun {}?\n".format(luku1)))
        summa = luku1 + luku2
        print("Vastaus on",summa)

    elif laskutapa == "erotus":
        luku1 = float(input("Mistä luvusta vähennetään?\n"))
        luku2 = float(input("Mitä vähennetään luvusta {}?\n".format(luku1)))
        erotus = luku1 - luku2
        print("Vastaus on",erotus)

    elif laskutapa == "tulo":
        luku1 = float(input("Mikä luku kerrotaan?\n"))
        luku2 = float(input("Millä luvulla kerrotaan luku {}?\n".format(luku1)))
        tulo = luku1 * luku2
        print("Vastaus on",tulo)

    elif laskutapa == "osamaara":
        luku1 = float(input("Mikä luku jaetaan?\n"))
        while True:
            luku2 = float(input("Millä luvulla jaetaan luku {}?\n".format(luku1)))
            if luku2 == 0:
                print("Nollalla ei voi jakaa. Anna toinen jakaja.")
            else:
                osamaara = luku1 / luku2
                print("Vastaus on",osamaara)
                break

    elif laskutapa == "peruuta":
        print("Näkemiin")
        break

    else:
        while True:
            ltapaj = input("Virheellinen laskutapa. Haluatko yrittää uudelleen (kyllä/ei)?\n")
            if ltapaj == "kyllä":
                break
            elif ltapaj == "ei":
                print("Näkemiin")
                exit()
            else:
                print("Vastaa kyllä tai ei.")
        continue

    while True:
        jatkumo = input("Haluatko laskea lisää (kyllä/ei)?\n")
        if jatkumo == "kyllä":
            break
        elif jatkumo == "ei":
            print("Kiitos laskimen käytöstä, näkemiin!")
            time.sleep(1)
            exit()
        else:
            print("Vastaa kyllä tai ei.")
