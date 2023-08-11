import create_note
import add_note
import change_note
import delete_note
import delete_all
import sorted_by_data_time
import read_file
import get_file_list
import path_to_file


# Критерии оценки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл (Create), уметь читать данные из файла(Show), делать выборку по дате(Sorted_time),
# выводить на экран выбранную запись(Show_1),
# выводить на экран весь список записок (Show) or (GetList),
# добавлять записку(Add), редактировать(Change) ее и удалять(Delete) or (Delete_all).

def get_info_from_user():
    print("Введите команду:")
    comand = input()

    match comand:
        case "Create":
            # создает новый файл и добавляет 2 строки,
            # 1- ключи, 2 - сами значения, по ключам,
            # если нужно добавить еще одну запись - воспользуйтесь командой Add
            note_name = input("Введите название файла:")
            note_data = input("Введите содержание заметки:")
            create_note.create_note(note_name, note_data)
            read_file.get_current_note(file_name=note_name, current_num=1)
        case "Add":  # добавляет новую запись в конец файла
            note_name = input("Введите название файла:")
            note_data = input("Введите новое содержание заметки:")
            add_note.add_note(note_name, note_data)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Change":
            # меняет содержание любой строки начиная со 2 в файле,
            # в первой строке находятся ключи
            print("Что-бы узнать номер строки, используйте команду Show")
            note_name = input("Введите название файла:")
            note_row_number = input("Введите номер строки:")
            change_note.change_note(note_name, note_row_number)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Delete":
            # удаляет только выбранную строку в файле, но не весь файл
            note_name = input("Введите название файла:")
            note_row_number = input("Введите номер строки:")
            delete_note.delete_note(note_name, note_row_number)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Delete_all":  # удаляет весь файл - целиком
            note_name = input("Введите название файла:")
            delete_all.delete_all(note_name)
            print(f"Заметка была удалена")
        case "Show":  # выводит список заметок
            note_name = input("Введите название заметки:")
            read_file.show_all(note_name)
        case "Show_1": # выводит запись с определенным номером строки
            note_name = input("Введите название файла:")
            note_row_number = input("Введите номер строки:")
            print(read_file.get_current_note(note_name, note_row_number))
        case "Sorted_time":  # сортирует по времени + дате
            note_name = input("Введите название файла:")
            sorted_by_data_time.sort_by_datetime(note_name)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "Sorted_csv":
            # удаляет пустые строки внутри файла .csv,
            # они появляются в результате удаления ненужных строк
            note_name = input("Введите название файла:")
            sorted_by_data_time.sort_csv(note_name)
            num = read_file.get_note_number(file_name=note_name)
            read_file.get_current_note(file_name=note_name, current_num=num)
        case "GetList":  # выводит список файлов в каталоге, папке, директории
            get_file_list.get_file_list()


get_info_from_user()
