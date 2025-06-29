#!/usr/bin/env python3
# combine_code.py
"""
Скрипт объединяет содержимое заданных Python-файлов в один текстовый
файл `combined.txt`, оборачивая каждый исходный код в теги <code_block>.
"""

from pathlib import Path
import sys

def combine_scripts(script_paths, output_path: Path = Path("combined.txt")) -> None:
    """
    Читает каждый файл из script_paths и записывает всё в output_path
    в формате <code_block> … </code_block>.

    :param script_paths: iterable[str | Path] — пути к исходным скриптам
    :param output_path: Path — путь к итоговому текстовому файлу
    """
    # Открываем файл на перезапись сразу, чтобы сбросить прежнее содержимое
    with output_path.open("w", encoding="utf-8") as out_file:
        for script in map(Path, script_paths):
            try:
                code = script.read_text(encoding="utf-8")
            except FileNotFoundError:
                print(f"⚠️  Файл не найден: {script}", file=sys.stderr)
                continue

            out_file.write("<code_block>\n")
            out_file.write(code.rstrip())        # уберём лишний перевод строки в конце
            out_file.write("\n</code_block>\n\n") # двойной \n для разделения блоков

    print(f"✅ Готово! Итог сохранён в {output_path.resolve()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python combine_code.py main.py AI.py utils/helpers.py ...")
        sys.exit(1)

    combine_scripts(sys.argv[1:])
