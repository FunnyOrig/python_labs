# Задание A - модуль **src/lab04/io_txt_csv.py**

Реализовано чтение текстовых файлов и запись CSV файлов.

```python
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
```

## 1. **read_text**

Функция читает файл и возвращает его содержимое в виде одной строки. По умолчанию используется кодировка UTF-8, однако возможность поменять кодировку на другую присутствует.

## 2. **write_csv**

Функция записывает строки в CSV-файл. Перед записью проверяется, что все строки имеют одинаковую длину. Если длины отличаются, вызывается ValueError. Если передан параметр header, он записывается первой строкой файла.

## 3. **ensure_parent_dir**

Функция проверяет наличие родительской папки и создает ее вместе со всеми отсутствующими папками по пути.

## Пример запуска (С header'ом)

![](../../images/lab04/check_csv.png)

# Задание B - скрипт **src/lab04/text_report.py**

Скрипт читает текстовые файлы, использует функции normalize, tokenize, count_freq и top_n из лабораторной работы №3, а затем сохраняет частоты слов в CSV-файлы.

```python
from pathlib import Path
import argparse
import sys

ROOT_DIR = Path(__file__).resolve().parents[2]
SRC_DIR = Path(__file__).resolve().parents[1]

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv

DATA_DIR = ROOT_DIR / "data"


def main():
    parser = argparse.ArgumentParser(
        description="Создание CSV-отчёта по частоте слов."
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        type=Path,
        default=DATA_DIR / "input.txt",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        type=Path,
        default=DATA_DIR / "report.csv",
    )

    args = parser.parse_args()

    input_path = args.input_path
    if not input_path.is_absolute():
        input_path = ROOT_DIR / input_path

    text = read_text(input_path, encoding=args.encoding)
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    freq = count_freq(tokens)

    write_csv(
        top_n(freq, len(freq)),
        path=args.output_path,
        header=("word", "count")
    )

    top_5 = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top_5:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```

## Пример запуска

```bash
python src/lab04/text_report.py
```
Вывод:

![](../../images/lab04/text_report.png)

## Кодировка cp1251

```bash
python src/lab04/text_report.py --in data/lab04/input.txt --encoding cp1251
```
Вывод:

![](../../images/lab04/cp1251.png)