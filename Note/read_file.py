import csv
import path_to_file


def read_notes(file_name):
    path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)
    if not path_to_file.check_file(path_to_note):
        print("Файла с таким именем {},не существует".format(path_to_note))
        print("Попробуйте его создать, командой Create ")
        return []
    with open(path_to_note, "r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file, delimiter="/"))


def get_note_number(file_name):
    notes = read_notes(file_name)
    try:
        return notes[-1]["Номер Заметки"] if notes else -1
    except KeyError as error:
        return f"Ключа с таким именем {error},не существует, вы удалили первую строку"


def get_current_note(file_name, current_num):
    notes = read_notes(file_name)
    try:
        for row in notes:
            if row["Номер Заметки"] == current_num:
                return row["Номер Заметки"] + ": " + row["Тело Заметки"]
        return "Не существует"
    except KeyError as error:
        return f"Ключа с таким именем {error},не существует, вы удалили первую строку"


def show_all(file_name):
    notes = read_notes(file_name)

    try:
        count = 2
        for row in notes:
            print(
                " Номер Строки = " + str(count) +
                " Номер Заметки = " + row["Номер Заметки"] + " : " +
                "Тело Заметки = " + row["Тело Заметки"])
            count += 1
        return notes
    except KeyError as error:
        print(f"Ключа с таким именем {error},не существует, вы удалили первую строку")

