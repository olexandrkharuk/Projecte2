hi_ha_negatiu = False
for i in range(10):
    num = int(input("Introdueix un nom: "))
    if num < 0:
        hi_ha_negatiu = True
if hi_ha_negatiu:
    print("Hi ha al menys un nom negatiu")
else:
    print("No hi ha cap nombre negatiu")