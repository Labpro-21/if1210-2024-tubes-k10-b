from typing import List, TextIO


def readlines(path: str) -> List[str]:
    data: TextIO = open(path, 'r')
    n: int = 0
    for _ in data:
        n += 1
    data.close()
    data: TextIO = open(path, 'r')
    arr: List[str] = ["" for _ in range(n)]
    idx: int = 0
    for i in data:
        arr[idx] = i
        idx += 1
    data.close()
    return arr
