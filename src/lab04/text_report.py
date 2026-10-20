
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
        help="Кодировка входного файла, например cp1251"
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        type=Path,
        default=DATA_DIR / "input.txt",
        help="Входной файл"
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        type=Path,
        default=DATA_DIR / "report.csv",
        help="Выходной CSV-отчёт"
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