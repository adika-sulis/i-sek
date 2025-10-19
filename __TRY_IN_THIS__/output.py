import os
# os.system("cls")

elsőSzám = float(input("Add meg az első számot!   "))
másodikSzám = float(input("Add meg a MÁSODIK számot!   "))
művelet = input("Add meg a műveletet!\n  Összeadás (+) | Kivonás (-) | Szorzás (*) | Osztás (÷ vagy /)  ")

# eredmény = elsőSzám + másodikSzám
# print(f"A két szám összege {eredmény}")

if művelet == "+":
    eredmény = elsőSzám + másodikSzám
    print(f"\nA két szám összege: {eredmény}")
elif művelet == "-":
    eredmény = elsőSzám - másodikSzám
    print(f"\nA {elsőSzám}-ból/ből kivonva {másodikSzám} eredmény: {eredmény} ")
elif művelet == "*":
    eredmény = elsőSzám * másodikSzám
    print(f"\nA két szám szorzata: {eredmény}")
elif művelet == "÷" or művelet == "/":
    eredmény = elsőSzám / másodikSzám
    print(f"\nAz {elsőSzám} elosztva {másodikSzám}-val/vel eredménye: {eredmény}")
else:
    print("\nNekem te ne emberkedel! Add meg művelet te csicskusz!")


