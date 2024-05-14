from typing import List, TextIO, Tuple

Matrix = List[List[str]]


def get_peta(folder_name: str) -> Tuple[int, int, Matrix]:
    file: TextIO = open("./data/%s/peta.txt" % (folder_name))
    arr: List[str] = []
    for i in file:
        arr.append(i)
    file.close()
    n: int = int(arr[0])-2
    m: int = int(arr[1])-1
    peta: Matrix = [["" for _ in range(m)] for _ in range(n)]
    for i in range(2, 2+n):
        for j in range(m):
            peta[i-2][j] = arr[i][j]
    return (n, m, peta)


def mapify(peta: Matrix) -> None:
    row: int = len(peta)
    col: int = len(peta[0])
    for i in range(col+2):
        print(end="* ")
    print()
    for i in range(row):
        for j in range(col):
            if j == 0:
                print(end="* ")
            print(peta[i][j] if peta[i][j] != '#' else " ", end=" ")
            if j == col-1:
                print(end="* ")
        print()
    for i in range(col+2):
        print(end="* ")
