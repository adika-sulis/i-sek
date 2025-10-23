import os
import re

os.system("cls")

# Script és mappa elérési útjai 
script_dir = os.path.dirname(os.path.abspath(__file__))  # ahol a script van 
parent_dir = os.path.dirname(script_dir)                 # szülőmappa
coms_path = os.path.join(parent_dir, "coms.txt")

if not os.path.exists(coms_path):
    print(f"\n⚠️ Nem található a coms.txt a szülőmappában: {coms_path}")
    exit()

# coms betöltése 
coms = {}
with open(coms_path, encoding="utf-8") as f:
    for line in f:
        if "=" not in line or line.strip().startswith("#"):
            continue
        key, val = line.strip().split("=", 1)
        key = key.strip('"')
        coms[key] = val


fajlok = [f for f in os.listdir(script_dir) if f.endswith(".i-sek")]

if not fajlok:
    print(f"\n⚠️ Nincsenek .i-sek fájlok a script mappájában: {script_dir}")
    exit()

print("\n\n📂 Elérhető .i-sek fájlok:")
for i, fajl in enumerate(fajlok, start=1):
    print(f"   {i}. {fajl}")

# fájl kiválasztása
while True:
    valasz = input("\nAdd meg a fájl számát:   ").strip()
    if not valasz:
        exit()
    elif valasz.lower() == "clear":
        with open(os.path.join(script_dir, "output.py"), "w", encoding="utf-8") as c:
            c.write("")
            print("\nTörölve: output.py\nKilépés...")
            exit()
    try:
        valasztas = int(valasz)
        if 1 <= valasztas <= len(fajlok):
            kivalasztott = fajlok[valasztas - 1]
            break
        else:
            print(f"Kérlek, 1 és {len(fajlok)} közötti számot adj meg!")
    except ValueError:
        print("Érvénytelen bemenet — csak számot adj meg!")

os.system("cls")
print("\n<---------------------------------->\n")

# fájl beolvasása
with open(os.path.join(script_dir, kivalasztott), encoding="utf-8") as f:
    code = f.read()

# coms csereeeee
for key in sorted(coms.keys(), key=len, reverse=True):
    val = coms[key]
    pattern = rf"(?<!\w){re.escape(key)}(?!\w)"
    code = re.sub(pattern, val, code)

# outputoling xd
output_path = os.path.join(script_dir, "output.py")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(code)

# lefut
os.system(f"python \"{output_path}\"")

print("\n<---------------------------------->")
input(" 🔚 Nyomj Entert a kilépéshez...   ")
