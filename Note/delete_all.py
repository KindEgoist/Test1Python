import os
import path_to_file


def delete_all(file_name):
    path_to_note = path_to_file.get_path_to_file(path_to_file.directory_name, file_name)
    try:
        os.remove(path_to_note)
        print("Файл успешно удален")
    except Exception:
        print("Файла не существует")

