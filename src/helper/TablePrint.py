from typing import List, TextIO
from helper.Splitter import splitter


def table_print(data: List[str]) -> None:
    n: int = len(data)
    m: int = len(splitter(data[0]))
    table_length: List[int] = [0 for _ in range(m)]
    for i in range(n):
        for j in range(m):
            table_length[j] = max(table_length[j], len(splitter(data[i])[j]))

    for i in range(n):
        for j in range(m):
            element: str = splitter(data[i])[j]
            print("| %s " % (element), end="")
            for k in range(table_length[j]-len(element)):
                print(end=" ")
        print("|")
