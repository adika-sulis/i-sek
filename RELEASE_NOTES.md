# i-sek v0.1.0 — Első kiadás

**Tag:** v0.1.0  
**Target branch:** main  
**Prerelease:** nem

## Rövid összefoglaló
Az i-sek egy kísérleti forrásszintaxis, amely magyar kulcsszavakat használ, és Python kódra fordítható. Ez az első hivatalos kiadás tartalmazza a kulcsszó-térképet és a dokumentációt, amely lefedi a magyar → Python leképezéseket.

## Főbb újdonságok
- **Added:** Teljes kulcsszó-térkép a README-ben, amely a magyar kulcsszavakat a megfelelő Python konstrukciókra térképezi. Példák a térképből:
  - `bölcsesség` → `print`
  - `ajtóKinyit` → `import`
  - `beenged` → `from`
  - `haha` → `if`, `haha'nt` → `else`, `hahaIsNem` → `elif`
  - `nyit` → `for`, `nézzKörül` → `range`, `irniFuzetbe` → `while`
  - `függöny` → `def`, `hozdVissza` → `return`
  - operátorok és beépített függvények: `hozdÖssze`(+), `jóóHosszú`→`len`, `brüsszeliGurulóDollárok`→`.append`, `töröldKi`→`.remove` stb.
- **Documentation:** README részletes leírást és kulcsszó-térképet tartalmaz.
- **Includes:** coms.txt további megjegyzéseket/példákat tartalmazhat a használathoz.

## Példa használat

Egy egyszerű i-sek sor:
```isek
bölcsesség("Hello i-sek")
```

Fordítva (Python):
```python
print("Hello i-sek")
```

Vezérlési szerkezet példa i-sek-ben:
```isek
haha feltétel:
    bölcsesség("IGEN")
haha'nt:
    bölcsesség("NEM")
```

Fordítva (Python):
```python
if feltétel:
    print("IGEN")
else:
    print("NEM")
```

## Telepítés és kipróbálás
1. Klónozd a repót:
   git clone https://github.com/adika-sulis/i-sek.git
2. Nyisd meg a README.md fájlt a teljes kulcsszó-térképért és példákért.
3. Nézd át a `__TRY_IN_THIS__` könyvtárat (ha tartalmaz fájlokat) a gyorsteszthez.

## Ismert korlátok
- Ez az első kiadás elsősorban a kulcsszó-térképre és dokumentációra fókuszál. Ha vannak fordító/futtató eszközök a repóban, azok állapota és funkcionalitása a fájlok alapján eltérő lehet.
- Nincsenek ismert breaking change-ek erre a verzióra (első kiadás).

## Contributing
Változás- és új kulcsszó-javaslatokat, fordító fejlesztéseket szívesen fogadunk — nyiss egy issue-t vagy küldj PR-t.

## Licenc
A projekt licencére vonatkozó részletek a repository `LICENSE` fájljában találhatók.

## Köszönet
Köszönet minden korai tesztelőnek és hozzájárulónak — a README és a coms.txt nagyban segítettek a jelen kiadás összállításában.