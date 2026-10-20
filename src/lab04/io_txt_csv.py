from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv( rows: Iterable[Sequence],
               path: str | Path, 
               header: tuple[str, ...] | None = None) -> None:
    rows = list(rows)

    expected_length = (
    len(rows[0])
    if rows
    else len(header) if header is not None
    else None
)

    if rows:
        for index, row in enumerate(rows, start=1):
            if len(row) != expected_length:
                raise ValueError(
                    f"Строка {index} содержит {len(row)} значений, "
                    f"ожидалось {expected_length}."
                )
            
    p = Path(path)

    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

# Тесты
#txt = read_text(r"C:\Users\Honor\OneDrive\Documents\GitHub\python_labs\data\input.txt")  # должен вернуть строку
#print(txt)
#write_csv([("word","count"),("test",3)], "data/check.csv", header= (["что-то"])) # Создаст CSV