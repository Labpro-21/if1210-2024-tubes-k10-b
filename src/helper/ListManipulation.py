from typing import List, TextIO
from .Splitter import splitter


def table_print(data: List[List[str]]) -> None:
    """
    Prosedur ini membutuhkan parameter list 2 dimensi yang nantinya 
    akan diproses menjadi sebuah tabel yang rapih dengan mengeluarkan 
    output di terminal.
    """
    n: int = len(data)
    m: int = len(data[0])
    table_length: List[int] = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            table_length[j] = max(table_length[j], len(data[i][j]))

    for i in range(n):
        for j in range(m):
            element: str = data[i][j]
            print("| %s " % (element), end="")
            for k in range(table_length[j]-len(element)):
                print(end=" ")
        print("|")


def to_list(data: List[str]) -> List[List[str]]:
    """
    Fungsi ini digunakan untuk memproses list 1 dimensi menjadi 2 dimensi

    Contoh input: ["ID;Type;Stock", "0;Ayam;1"] 
    Contoh output: [["ID","Type","Stock"], ["0","Ayam","1"]]
    """
    row: int = len(data)
    col: int = len(splitter(data[0]))
    arr: List[List[str]] = [["" for _ in range(col)] for _ in range(row)]
    for i in range(row):
        tmp: List[str] = splitter(data[i])
        for j in range(col):
            arr[i][j] = tmp[j]
    return arr


def bubble_sort(data: List[str]) -> None:
    """
    Prosedur bubble_sort digunakan untuk mengurutkan list menggunakan 
    algoritma bubble sort. 

    contoh penggunaan:
    >>> arr = [1,2,5,4,3]
    >>> bubble_sort(arr)
    >>> print(arr)
    [1,2,3,4,5]
    """
    n: int = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

def join(data: List[str]) -> str:
    txt: str = ""
    col: int = len(data)
    for i in range(col):
        txt += data[i]
        if i != col-1:
            txt += ';'
    return txt