from typing import List


def count_delimiter(data: str) -> int:
    count: int = 0
    for i in data:
        if i == ';':
            count += 1
    return count


def result(n: int, arr: List[str], idx: int, data: str, pos: int) -> None:
    if pos == n+1:
        return
    elem: str = ""
    while data[idx] != ';' and data[idx] != '\n':
        elem += data[idx]
        idx += 1
    arr[pos] = elem
    result(n, arr, idx+1, data, pos+1)


def splitter(data: str) -> List[str]:
    n: int = count_delimiter(data)
    arr: List[str] = ["" for _ in range(n+1)]
    result(n, arr, 0, data+";", 0)
    return arr
