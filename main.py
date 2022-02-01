'''
Bejelentkezés

Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! 
A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. 
A program egyetlen felhasználó (bori99) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. 
Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Szivecske<3
Belépés engedélyezve.
-----
Adja meg a felhasználónevét! Bagaméri
Adja meg a jelszavát! A kankalin sötétben virágzik!
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! hibásjelszó
Belépés megtagadva.
Adja meg a felhasználónevét! hibásfelhasználó
Adja meg a jelszavát! Szivecske<3
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Szivecske<3
Belépés engedélyezve.
'''
jelszo = "Szivecske<3"
felhasznalo = "bori99"

while True:
  jel_tipp = input("Adja meg a felhasználónevét! ")
  fel_tipp = input("Adja meg a jelszavát! ")
  if jelszo == jel_tipp and felhasznalo == fel_tipp:
    print("Belépés engedélyezve.")
    break
  else:
    print("Belépés megtagadva.")
