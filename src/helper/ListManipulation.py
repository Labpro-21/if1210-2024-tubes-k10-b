from typing import List, TextIO
from .Splitter import splitter


def table_print(data: List[List[str]]) -> None:
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
    row: int = len(data)
    col: int = len(splitter(data[0]))
    arr: List[List[str]] = [["" for _ in range(col)] for _ in range(row)]
    for i in range(row):
        tmp: List[str] = splitter(data[i])
        for j in range(col):
            arr[i][j] = tmp[j]
    return arr
