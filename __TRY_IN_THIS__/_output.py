import os
# os.system("cls")
művelet = 0

while True :
    elsőSzám = input("Add meg az első számot!   ")
    if not elsőSzám :
        break
    elsőSzám = float(elsőSzám)
    másodikSzám = input("Add meg a MÁSODIK számot!   ")
    if not másodikSzám :
        break
    másodikSzám = float(másodikSzám)
    művelet = input("Add meg a műveletet!\n  Összeadás (+) | Kivonás (-) | Szorzás (*) | Osztás (÷ vagy /)  ")
    if not művelet :
        break
    break

""" 
eredmény = elsőSzám + másodikSzám
print(f"A két szám összege {eredmény}")
"""

if művelet == "+" :
    eredmény = elsőSzám + másodikSzám
    print(f"\nA két szám összege : {eredmény}")
    # print ugyanúgy print mint a print
elif művelet == "-" :
    eredmény = elsőSzám - másodikSzám
    print(f"\nA {elsőSzám}-ból/ből kivonva {másodikSzám} eredmény : {eredmény}")
elif művelet == "*" :
    eredmény = elsőSzám * másodikSzám
    print(f"\nA két szám szorzata : {eredmény}")
elif művelet == "÷" or művelet == "/" :
    eredmény = elsőSzám / másodikSzám
    print(f"\nAz {elsőSzám} elosztva {másodikSzám}-val/vel eredménye : {eredmény}")
else :
    print("\nNekem te ne emberkedel! Add meg művelet te csicskusz!")

