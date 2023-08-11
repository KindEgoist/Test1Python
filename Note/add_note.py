import csv
import path_to_file
import read_file


def add_note(file_name, add_note):
    count = int(read_file.get_note_number(file_name))

    path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)

    data = {"Номер Заметки": count + 1,
            "Дата": f"{path_to_file.get_time()[0]}",
            "Время": f"{path_to_file.get_time()[1]}",
            "Тело Заметки": add_note}

    if path_to_file.check_file(path_to_note):
        with path_to_file.open_csv_file(file_name, "a") as file:
            column = ["Номер Заметки", "Дата", "Время", "Тело Заметки"]
            note_writer = csv.DictWriter(file, fieldnames=column, delimiter="/")
            note_writer.writerow(data)
            print(f"Заметка {file_name} добавлена")


