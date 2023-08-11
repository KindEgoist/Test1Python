import os
import path_to_file


def get_file_list():
    with os.scandir():
        for entry in os.scandir(path_to_file.directory_name):
            if entry.is_file() and entry.name.endswith(".csv"):
                print(entry.name)

