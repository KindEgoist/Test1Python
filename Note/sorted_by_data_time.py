import csv
import path_to_file


def sort_by_datetime(file_name):
    try:
        with path_to_file.open_csv_file(file_name, "r") as file:
            reader = csv.reader(file, delimiter="/")
            header = next(reader)
            rows = list(reader)

        sorted_rows = sorted(rows, key=lambda row: (row[1], row[2]))

        with path_to_file.open_csv_file(file_name, "w") as file:
            writer = csv.writer(file, delimiter="/")
            writer.writerow(header)
            writer.writerows(sorted_rows)
            print(f"Заметка {file_name} была отсортирована")
    except FileNotFoundError as error:
        print(f"{error}")
    except Exception as ex:
        print(f"{ex}")


def sort_csv(file_name):
    try:
        with path_to_file.open_csv_file(file_name, "r") as file:
            reader = csv.reader(file, delimiter="/")
            rows = [row for row in reader if any(field.strip() for field in row)]

        with path_to_file.open_csv_file(file_name, "w") as file:
            writer = csv.writer(file, delimiter="/")
            writer.writerows(rows)
            print(f"Заметка {file_name} была отсортирована")
    except Exception as ex:
        print(f"{ex}")
