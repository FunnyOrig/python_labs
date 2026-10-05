def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента.

    rec:
        (ФИО, группа, GPA)

    ФИО должно содержать фамилию и имя, либо фамилию,
    имя и отчество. Лишние пробелы удаляются.

    GPA должен быть числом от 0.0 до 5.0.

    Raises:
        ValueError: если ФИО или группа пустые, либо GPA вне диапазона.
        TypeError: если GPA имеет неправильный тип.
    """

    fio, group, gpa = rec

    # Убираем лишние пробелы
    fio = " ".join(fio.strip().split())
    group = " ".join(group.strip().split())

    # Проверяем ФИО и группу
    if not fio:
        raise ValueError("ФИО не может быть пустым")

    if not group:
        raise ValueError("Группа не может быть пустой")

    # Проверяем GPA
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0.0 до 5.0")

    # Разделяем ФИО на части
    parts = fio.split()

    if len(parts) < 2:
        raise ValueError("ФИО должно содержать хотя бы фамилию и имя")

    if len(parts) > 3:
        raise ValueError("ФИО должно содержать не более трёх частей")

    surname = parts[0].capitalize()

    # Берём инициалы имени и отчества
    initials = ""

    for part in parts[1:]:
        initials += part[0].upper() + "."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))