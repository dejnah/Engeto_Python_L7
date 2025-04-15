### CVIČENÍ, Vyzkoušej si práci s *uživatelskými funkcemi*:
# 1. Nahraj knihovnu `random`,
# 2. vytvoř definici uživatelské funkce `vygeneruj_tuple`,
# 3. funkce potřebuješ zadat **dva celočíselné parametry** `delka` a `max_hodnota`,
# 4. funkce vrací datový typ `tuple`,
# 5. obecným účelem funkce je vrátit takový *tuple*, který má délku podle `delka` a rozsah náhodných celých čísel je z intervalu `0 ~ max_hodnota`,
# 6. nakonec funkci zavolej pro tyto argumenty: `5, 50`, `10, 100` a `15, 150` (pro parametry `delka`, `max_hodnota`).


from random import choices

def vygeneruj_tuple(delka, max_hodnota):
    return tuple(choices(range(max_hodnota + 1), k=delka))

print(
    vygeneruj_tuple(5, 50),
    vygeneruj_tuple(10, 100),
    vygeneruj_tuple(15, 150),
    sep="\n"
)
