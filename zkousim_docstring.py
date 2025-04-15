### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s docstringy v *uživatelských funkcích*:

# 1. Vytvoř takovou *uživatelskou funkci*, která potřebuje jeden *parametr* `udaje` (typu `tuple`),
# 2. funkce musí opět vracet typ `tuple`,
# 3. jejím účelem je odstranit ze zadaného argumentu všechny `None` hodnoty a vrátit zbytek,
# 4. vhodně **funkci pojmenuj**,
# 5. napiš krátký *docstring*, který pomůže funkci lépe dovysvětlit.

krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)

# def XYZ(udaje: tuple) -> tuple:
#     """
#     Funkce vrací zadanou sekvenci bez prázdný/ chybějících hodnot
#     """

# print(
#     XYZ(krestni_jmena),
#     XYZ(prijmeni),
#     sep='\n'
# )

krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)


def filtruj_prazdne_hodnoty(udaje: tuple) -> tuple:
    """
    Funkce vrací pole hodnot bez prázdných hodnot.

    :param udaje: Zadané pole, které může obsahovat prázdné hodnoty,
    :type udaje: tuple
    :return: pole bez prázdných hodnot,
    :rtype: tuple
    """
# zkrácený zápis comprehension    
    return tuple(
        hodnota for hodnota in udaje
        if hodnota
    )

# nezkrácený zápis podmínky výš

# vysledek = []
# for hodnota in udaje:
#     if hodnota:
#        vysledek.append(hodnota)
#
# return tuple(vysledek)

print(
    filtruj_prazdne_hodnoty(krestni_jmena),
    filtruj_prazdne_hodnoty(prijmeni),
    sep="\n"
)
