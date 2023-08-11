import csv
import path_to_file


def create_note(file_name, input_note):
    path_to_file.check_directory(path_to_file.directory_name)

    path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)

    if path_to_file.check_file(path_to_note):
        print(f"Файл с таким именем {file_name}, уже существует")
        return -1

    data = [{"Номер Заметки": 1,
             "Дата": f"{path_to_file.get_time()[0]}",
             "Время": f"{path_to_file.get_time()[1]}",
             "Тело Заметки": input_note}
            ]

    with path_to_file.open_csv_file(file_name, "w") as file:
        column = ["Номер Заметки", "Дата", "Время", "Тело Заметки"]
        note_writer = csv.DictWriter(file, fieldnames=column, delimiter="/")
        note_writer.writeheader()
        note_writer.writerows(data)
        print(f"Заметка {file_name} создана")


