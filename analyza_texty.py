"""
projekt_1.py: první projekt do Engeto Online Python Akademie

Autor: Stanislava Jahodová
Email: stanislavajahodova@gmail.com
"""

# === TEXTY K ANALÝZE ===
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# === REGISTROVANÍ UŽIVATELÉ ===
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# === PŘIHLÁŠENÍ ===
jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")

print(f"uživatelské jméno: {jmeno}")
print(f"heslo: {heslo}")

if jmeno not in uzivatele or heslo != uzivatele[jmeno]:
    print("Neregistrovaný uživatel – ukončuji program.")
    exit()

# === UVÍTÁNÍ ===
oddelovac = "-" * 42
print(f"{oddelovac}\nVítej v naší aplikaci, {jmeno.title()}.\n{oddelovac}")
print(f"Máme pro tebe na výběr {len(TEXTS)} texty k analýze.\n{oddelovac}")

# === VÝBĚR TEXTU ===
volba = input(f"Zadej číslo 1-{len(TEXTS)}: ")
print(f"{volba}\n{oddelovac}")

if not volba.isdigit():
    print("Nebyl zadán platný číselný vstup – ukončuji program.")
    exit()

volba = int(volba)
if not (1 <= volba <= len(TEXTS)):
    print("Číslo je mimo rozsah – ukončuji program.")
    exit()

# === ANALÝZA TEXTU ===
text = TEXTS[volba - 1]
slova = [slovo.strip(",.-;'") for slovo in text.split()]

print("Ve zvoleném textu je:")
print(f"Celkový počet slov: {len(slova)}")
print(f"Počet slov začínajících velkým písmenem: {len([s for s in slova if s.istitle()])}")
print(f"Počet slov psaných VELKÝMI písmeny: {len([s for s in slova if s.isupper()])}")
print(f"Počet slov psaných malými písmeny: {len([s for s in slova if s.islower()])}")

cisla = [int(s) for s in slova if s.isdigit()]
print(f"Počet čísel: {len(cisla)}")
print(f"Suma všech čísel: {sum(cisla)}\n{oddelovac}")

# === GRAF ČETNOSTI DÉLEK SLOV ===
print(f"{'DELKA':>6}|{'VÝSKYT':^18}| POČET\n{oddelovac}")

vyskyt = {}
for slovo in slova:
    delka = len(slovo)
    vyskyt[delka] = vyskyt.get(delka, 0) + 1

for delka in sorted(vyskyt):
    hvezdy = '*' * vyskyt[delka]
    print(f"{delka:>6}|{hvezdy:<18}| {vyskyt[delka]}")