# Zadanie 1

def suma_listy(l):
    if not l:
        return 0
    else:
        return l[0] + suma_listy(l[1:])

my_list = [1, 2, 3, 4, 5]
print(suma_listy(my_list))

# funkcja suma_listy(l)
#   czy l jest puste?
#       y -> zwróć 0
#       n -> zwróć l[0] + suma_listy(lista_bez_0_elementu)

# Zadanie 2

def znajdz_najwiekszy_element_listy(l):
    if len(l) == 1:
        return l[0]
    else:
        max_rest = znajdz_najwiekszy_element_listy(l[1:])
        if l[0] > max_rest:
            return l[0]
        else:
            return max_rest

my_list = [7, 2, 9, 3, 5, 1]
print(znajdz_najwiekszy_element_listy(my_list))

# funkcja znajdz_najwiekszy_element_listy(l)
#   czy l ma wiecej niż 1 element?
#       y -> zwróć l[0]
#       n -> zwróć l[0] w wypadku gdy jest najwieksze
#       lub znajdz_najwiekszy_element_listy(lista_bez_0_elementu)

# Zadanie 3

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

for i in range(7):
    print(silnia(i))

# funkcja silnia(n)
#   czy n jest równe 0?
#       y -> zwróć 1
#       n -> zwróć n * silnia(n-1)

# Zadanie 4

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

# funkcja fibonacci(n)
#   czy n jest mniejsze od 1?
#       y -> zwróć n
#       n -> zwróć fibonacci(n-1) + fibonacci(n-2)

# Zadanie 5

def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 2 == 0:
            print("- - - - ")
        for j in range(len(sudoku)):
            if j % 2 == 0:
                print("|", end=" ")
            print(sudoku[i][j], end=" ")
            if j == len(sudoku)-1:
                print("|")
    print("- - - - ")

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def valid(sudoku, num, pos):
    # check row
    for i in range(len(sudoku)):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False
    # check 2x2 box
    box_x = pos[1] // 2
    box_y = pos[0] // 2
    for i in range(box_y*2, box_y*2+2):
        for j in range(box_x*2, box_x*2+2):
            if sudoku[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(sudoku):
    empty = find_empty(sudoku)
    if not empty:
        return True
    else:
        row, col = empty
    for num in range(1, 5):
        if valid(sudoku, num, (row, col)):
            sudoku[row][col] = num
            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    return False

sudoku = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

sudoku[0][0] = 2
sudoku[0][2] = 1
sudoku[1][1] = 3
sudoku[1][3] = 4
sudoku[2][0] = 1
sudoku[2][2] = 4
sudoku[3][1] = 4
sudoku[3][3] = 3

print("Sudoku:")
print_sudoku(sudoku)

solve(sudoku)

print("Rozwiazanie:")
print_sudoku(sudoku)