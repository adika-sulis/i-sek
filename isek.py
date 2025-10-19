import os
import sys
import re

def load_replacements(filename: str) -> dict:
    """
    Betölti a kulcsszavakat egy fájlból.
    Formátum: baloldal=jobboldal (soronként)
    """
    replacements = {}
    if not os.path.exists(filename):
        print(f"⚠️ Nem található a szavak fájl: {filename}")
        return replacements

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # üres sorok, megjegyzések kihagyása
            if "=" in line:
                left, right = line.split("=", 1)
                replacements[left.strip()] = right.strip()
    return replacements

def isek_to_python(code: str, replacements: dict) -> str:
    """
    Lefordítja az I-SEK nyelvet Pythonra.
    - Hosszabb kulcsszavak előbb cserélve
    - Csak teljes szavak (\b) cserélve
    """
    # Kulcsszavak hossza szerint csökkenő sorrendbe
    sorted_replacements = sorted(replacements.items(), key=lambda x: len(x[0]), reverse=True)

    for old, new in sorted_replacements:
        pattern = r'\b' + re.escape(old) + r'\b'
        code = re.sub(pattern, new, code)

    return code

def find_isek_file() -> str | None:
    """Megkeresi az első .i-sek fájlt a mappában."""
    for filename in os.listdir():
        if filename.endswith(".i-sek"):
            return filename
    return None

def run_isek_file(filename: str, replacements: dict):
    """Beolvassa, lefordítja és lefuttatja a .i-sek fájlt."""
    with open(filename, "r", encoding="utf-8") as f:
        code = f.read()

    python_code = isek_to_python(code, replacements)

    with open("output.py", "w", encoding="utf-8") as f:
        f.write(python_code)

    # A fordított kód kiírása debughoz (tetszés szerint bekapcsolható)
    # print("➡️ Lefordított Python kód:")
    print("--------------------------------\n")
    # print(python_code)
    # print("--------------------------------\n")

    try:
        exec(python_code)
    except Exception as e:
        print(f"❌ Hiba a futtatás közben: {e}")

if __name__ == "__main__":
    replacements = load_replacements("coms.txt")

    if not replacements:
        print("⚠️ Nincs egyetlen szótárbejegyzés sem, a fordítás üres lesz!")

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = find_isek_file()

    if not filename:
        print("❌ Nem találok .i-sek fájlt a mappában!")
    else:
        print(f"📄 Fájl betöltve: {filename}\n")
        run_isek_file(filename, replacements)

    print("\n--------------------------------")
    input("🔚 Nyomj Entert a kilépéshez...")
