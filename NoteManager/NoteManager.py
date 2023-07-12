                                    # Задание:
# Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать 
# заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

# Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл, уметь читать данные из файла, 
# делать выборку по дате, выводить на экран выбранную запись, выводить на экран весь список записок, добавлять 
# записку, редактировать ее и удалять.

# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.

# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку 
# с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры 
# запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, 
# на усмотрение студента.

                                    # Реализация:
# Вы можете запустить эту программу из командной строки. Когда вы запускаете программу, она запрашивает у вас команду. 

# Доступны следующие команды:
# "create": запрашивает у вас заголовок и основную часть и создает новую заметку.
# "view": отображает все заметки.
# "edit": вам будет предложено ввести идентификатор заметки, а затем новый заголовок и основную часть. Если вы 
# нажмете enter, ничего не вводя, сохранится существующий заголовок или основная часть.
# "delete": запрашивает у вас идентификатор заметки и удаляет заметку с этим идентификатором.
# "exit": завершает работу с программой.

import json
import os
import datetime

class Note:
    def __init__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

class NoteManager:
    def __init__(self, filename="notes.json"):
        self.filename = filename
        if not os.path.isfile(filename):
            self.notes = []
        else:
            with open(self.filename, "r") as f:
                notes_json = json.load(f)
                self.notes = [Note(**note) for note in notes_json]

    def save_notes(self):
        with open(self.filename, "w") as f:
            notes_json = [note.__dict__ for note in self.notes]
            json.dump(notes_json, f)

    def create(self, title, body):
        id = self.notes[-1].id + 1 if self.notes else 1
        date = str(datetime.datetime.now())
        self.notes.append(Note(id, title, body, date))
        self.save_notes()

    def view(self):
        for note in self.notes:
            print(f"ID: {note.id}\nTitle: {note.title}\nBody: {note.body}\nDate: {note.date}\n---")

    def edit(self, id, new_title=None, new_body=None):
        for note in self.notes:
            if note.id == id:
                note.title = new_title if new_title else note.title
                note.body = new_body if new_body else note.body
                note.date = str(datetime.datetime.now())
                self.save_notes()
                return

    def delete(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_notes()

    def get_note_by_date(self, date):
        return [note for note in self.notes if note.date.startswith(date)]


def main():
    note_manager = NoteManager()
    while True:
        command = input("Введите комманду (create/view/edit/delete/exit): ")
        if command == "create":
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            note_manager.create(title, body)
        elif command == "view":
            note_manager.view()
        elif command == "edit":
            id = int(input("Введите идентификатор заметки: "))
            title = input("Введите новое название заголовка (нажмите enter, чтобы пропустить): ")
            body = input("Введите новый текст заметки (нажмите enter, чтобы пропустить): ")
            note_manager.edit(id, title or None, body or None)
        elif command == "delete":
            id = int(input("Введите идентификатор заметки: "))
            note_manager.delete(id)
        elif command == "exit":
            break
        else:
            print(f"Неизвестная комманда {command}")

if __name__ == "__main__":
    main()