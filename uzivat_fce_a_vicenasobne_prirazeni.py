### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *uživatelskými funkcemi* a *vícenásobné přiřazování*:

# 1. Nahraj knihovny `pprint` a `collections`,
# 2. vytvoř definici funkce `vyber_plnolete_klienty`, která potřebuje jedinný parametr `klient: tuple`,
# 3. tato funkce opět vrací datový typ `tuple`,
# 4. účelem funkce je projít zadané pole a vybrat pouze ty klienty, kteří jsou starší 18 let,
# 5. vrácenou hodnotu ulož do proměnné `plnoleti`,
# 6. z proměnné `plnoleti` přiřaď poslední záznam do proměnné `posledni_plnolety` pomocí vícenásobného přiřazování.

# pprint(posledni_plnolety)


from pprint import pprint
from collections import namedtuple

Klient = namedtuple('Klienti', field_names=['krestni_jmeno',
                                            'prijmeni',
                                            'email',
                                            'vek'])
vsichni_klienti = (
    Klient(krestni_jmeno='Matouš', prijmeni='Holinka', email='matous@holinka.com', vek=30),
    Klient(krestni_jmeno='Lukáš', prijmeni='Holinka', email='lukas.holinka@gmail.com', vek=20),
    Klient(krestni_jmeno='Petr', prijmeni='Svetr', email='psvetr@email.cz', vek=16),
    Klient(krestni_jmeno='Marek', prijmeni='Párek', email='parekm@seznam.cz', vek=14)
)


def vyber_plnolete_klienty(klienti: tuple) -> tuple:
    """
    Vrať nezměnitelné pole, které obsahuje jen takové klienty, kteří
    jsou stařší 18 let.

    :param klienti: Pole všech klientů,
    :type klienti: tuple
    :return: pole plnoletých klientů,
    :rtype: tuple
    """
    return tuple(klient for klient in klienti if klient.vek > 18)
        

plnoleti = vyber_plnolete_klienty(vsichni_klienti)
_ , posledni_plnolety = plnoleti # nebudu potřebovat ostatní proměnné, tak je zapíšu jako podtržítko

pprint(posledni_plnolety)
