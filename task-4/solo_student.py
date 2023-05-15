class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
         self.imie = imie
         self.nazwisko = nazwisko
         self.numer_indeksu = numer_indeksu
         self.oceny = [ 2 ]

    def __str__(self):
         return self.imie + " " + self.nazwisko

    def __int__(self):
        return 0

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny)

ocenySemestrPierwszy = [3, 4, 4, 4, 5]

student_Andrzej = Student("Andrzej", "Chorazy", 133777)
print(student_Andrzej)
print(student_Andrzej.oceny())

for ocena in ocenySemestrPierwszy(5):
    Student.dodaj_ocene(student_Andrzej, ocena)
