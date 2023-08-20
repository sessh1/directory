import os

DATA_FILE = "contacts.txt"


def add_contact():
    """
    Добавляет новую запись в справочник.

    Запрашивает у пользователя информацию о новом контакте (фамилия, имя,
    отчество, организация, рабочий телефон, личный телефон) и сохраняет её
    в текстовом файле.
    """
    print("Добавление новой записи:")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    organization = input("Организация: ")
    work_phone = input("Рабочий телефон: ")
    personal_phone = input("Личный телефон: ")

    with open(DATA_FILE, "a") as file:
        file.write(f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}\n")
    print("Запись добавлена")


def display_contacts(page_size=3):
    """
    Выводит записи из справочника постранично.

    page_size: Количество записей на странице (по умолчанию 3).
    """
    with open(DATA_FILE, "r") as file:
        contacts = file.readlines()

    total_contacts = len(contacts)
    num_pages = (total_contacts + page_size - 1) // page_size

    page = 1
    while page <= num_pages:
        print(f"Страница {page}/{num_pages}:")
        start_idx = (page - 1) * page_size
        end_idx = min(start_idx + page_size, total_contacts)
        for idx in range(start_idx, end_idx):
            print(contacts[idx].strip())
        page += 1
        input("Нажмите Enter для продолжения...")
        os.system("clear" if os.name == "posix" else "cls")


def edit_contact():
    """
    Редактирует существующую запись в справочнике.

    Запрашивает у пользователя строку для поиска (фамилию или имя), выводит
    совпадающие записи, позволяет выбрать одну для редактирования, после
    чего пользователь может ввести новые данные.
    """
    print("Редактирование записи:")
    search_term = input("Введите фамилию или имя для поиска: ").lower()

    with open(DATA_FILE, "r") as file:
        contacts = file.readlines()

    matching_contacts = []
    for contact in contacts:
        if search_term in contact.lower():
            matching_contacts.append(contact)

    if not matching_contacts:
        print("Записи не найдены")
        return

    for idx, contact in enumerate(matching_contacts):
        print(f"{idx + 1}. {contact.strip()}")

    choice = int(input("Введите номер записи для редактирования: ")) - 1
    if 0 <= choice < len(matching_contacts):
        edited_contact = matching_contacts[choice]
        new_data = input("Введите новые данные (фамилия,имя,отчество,организация,рабочий,личный): ")

        contacts[contacts.index(edited_contact)] = new_data + "\n"

        with open(DATA_FILE, "w") as file:
            file.writelines(contacts)

        print("Запись отредактирована")


def search_contacts():
    """
    Поиск записей в справочнике по заданным характеристикам.

    Позволяет пользователю ввести одну или несколько характеристик для поиска
    совпадающих записей. Выводит совпадающие записи на экран.
    """
    search_term = input("Введите одну или несколько характеристик для поиска: ").lower()

    with open(DATA_FILE, "r") as file:
        contacts = file.readlines()

    matching_contacts = []
    for contact in contacts:
        if any(term in contact.lower() for term in search_term.split()):
            matching_contacts.append(contact)

    if not matching_contacts:
        print("Записи не найдены")
        return

    for idx, contact in enumerate(matching_contacts):
        print(f"{idx + 1}. {contact.strip()}")


# Основной цикл программы
while True:
    print("1. Вывести записи")
    print("2. Добавить запись")
    print("3. Поиск записей")
    print("4. Редактировать запись")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        display_contacts()
    elif choice == "2":
        add_contact()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        break