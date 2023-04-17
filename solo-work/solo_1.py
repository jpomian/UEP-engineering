# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie:\n")

print("Hello "+student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi: "+str(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in range(len(studenci)):
    print("Hello " + studenci[i])

# zadanie 1.5

liczba = 3
potega = 4

wynik = 3**4

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: " + str(wynik))

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0
symbolToCount = "("

iterator = 0
for char in ciag_znakow:
    if char == symbolToCount:
        iterator += 1
    
print("Liczba nawiasow otwierajacych wynosi: " + str(iterator))

# zadanie 1.7


studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8


studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.9

studenci = ["John Smith", "Alice Brown", "Peter Johnson", "Emma White", "Nash Nitana", "Nicole Nielurna"]

nazwiskaNaN = []
for s in studenci:

    nazwisko = (lambda x: x.split()[-1])(s)
    
    if nazwisko.startswith("N"):
        nazwiskaNaN.append(nazwisko)

print(nazwiskaNaN)
print("Liczba studentów o nazwisku z N na początku: "  + str(len(nazwiskaNaN)))

# zadanie 1.10
def sprawdz_liniowosc(wykres):
    for i in range(len(wykres)):
        for j in range(i, len(wykres)):
            if (wykres[0, 0] == wykres[j, 0]):
                print("mamy to")
            else:
                print("nie ma")

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

sprawdz_liniowosc(wykres_1)
sprawdz_liniowosc(wykres_2)
sprawdz_liniowosc(wykres_3)

# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.