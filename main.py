import tkinter as tk
from datetime import datetime
from tkinter import filedialog
from docx import Document
from Document import MyDocument
import os

documents = []
id_ = 0
def open_word_file(id_, documents):
    file_path = filedialog.askopenfilenames(filetypes=[("Word Files", "*.docx")])
    if file_path:
        for path in file_path:
            doc = Document(path)
            doc_name = os.path.basename(path)
            doc_content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            doc_created_date = datetime.fromtimestamp(os.path.getctime(path)).strftime('%H:%M - %d.%m.%Y').split("-")
            #doc_modified_date = datetime.fromtimestamp(os.path.getmtime(path)).strftime('%H:%M - %d.%m.%Y').split("-")
            document = MyDocument(doc_name,doc_content,doc_created_date[1],doc_created_date[0],id_)
            id_+=1

            document.add_document_to_base(documents)
        print(documents)

# Создаем главное окно
root = tk.Tk()
root.title("Выбор Word-файла")

# Создаем кнопку для выбора файла
open_button = tk.Button(root, text="Добавить Word-документ", command=lambda : open_word_file(id_, documents))
open_button.pack()

# Создаем метку для вывода информации о файле
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
