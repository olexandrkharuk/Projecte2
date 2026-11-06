nota = 0
hi_ha_10 = False

while nota != -1:
    nota = int(input("Introdueix una nota (-1 per acabar): "))

    if nota == 10:
        hi_ha_10 = True

if hi_ha_10:
    print("Hi ha hagut alguna nota que té un 10")
else:
    print("No hi ha cap 10")