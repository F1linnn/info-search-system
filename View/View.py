import tkinter as tk

from Controller import Controller
class View:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Пример MVC с Tkinter")

        # Создаем кнопку для загрузки файла и размещаем ее внизу

        self.button = tk.Button(root, text="Загрузить Word файл", command=self.controller.open_word_file, width=60, height=2)
        self.button.grid(row=3, column=0, sticky='n', padx=10, pady=10)



        # Создаем текстовое поле для отображения информации о загруженных файлах
        self.log_text = tk.Text(root, height=15, width=60)
        self.log_text.grid(row=1, column=0, columnspan=2, padx=20, pady=(0,0), sticky='nw')
        self.log_text.config(state=tk.DISABLED)

        custom_font = ("Arial", 14)
        self.query_label = tk.Label(root, text="Панель результатов выполненных действий", padx=10, pady=5,
                                    font=custom_font)
        self.query_label.grid(row=0, column=0, padx=60, pady=7)

        self.label = tk.Label(root, text="Для начала работы загрузите файлы в формате docx",
                                    font=custom_font)
        self.label.grid(row=2, column=0, sticky='w', padx=25, pady=10)


        # Создаем метку для пояснительного текста
        self.query_label = tk.Label(root, text="Введите языковой запрос:", padx=10, pady=5, font=custom_font)
        self.query_label.grid(row=4, column=0)

        # Создаем поле для ввода языкового запроса
        self.query_entry = tk.Entry(root, width=44, font=custom_font)
        self.query_entry.grid(row=5, columnspan=2, padx=20, pady=(0,20), sticky='nw')


        # Создаем кнопку для выполнения запроса
        self.execute_button = tk.Button(root, text="Выполнить запрос", command=self.controller.start, width=60, height=2)
        self.execute_button.grid(row=6, column=0, padx=10, pady=10)


        # Задаем конфигурацию сетки для растяжения метки на всю доступную ширину
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def show_open_files_button(self):
        # Создаем метку для пояснительного текста
        custom_font = ("Arial", 14)
        self.query_label = tk.Label(self.root, text="Градация файлов", padx=10, pady=5,
                                    font=custom_font)
        self.query_label.grid(row=0, column=1, padx=60, pady=7)

        # Создаем кнопку для открытия файлов
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, width=60)
        self.listbox.grid(row=1, column=1, padx=20, pady=(0,0), sticky='nw')

        self.controller.update_file_list()


        self.open_files_button = tk.Button(self.root, text="Открыть файл", command=self.controller.open_new_files, font=custom_font)
        self.open_files_button.grid(row=1, column=1, columnspan=1, padx=10, pady=(0,20), sticky='s')

        self.show_metrics_button = tk.Button(self.root, text="Показать метрики и график", command=self.show_metrics_results, font=custom_font)
        self.show_metrics_button.grid(row=2, column=1, padx=10, pady=(0,60))

        self.query_label1 = tk.Label(self.root, text="Выберите файл", padx=10, pady=5,
                                    font=custom_font)
        self.query_label1.grid(row=3, column=1, columnspan=2, padx=60, pady=0)

        self.generate_annotation = tk.Button(self.root, text="Сгенерировать аннотацию", command=self.controller.generate_annotation, font=custom_font)
        self.generate_annotation.grid(row=4, column=1, columnspan=1, padx=10, pady=(0, 10), sticky='s')


    def show_metrics_results(self):
        # Создайте новое окно
        self.metrics_window = tk.Toplevel(self.root)
        self.metrics_window.title("Результаты метрик и график")

        # Добавьте компоненты (метрики и графики) в это окно
        # ...

        # Пример: добавление текстовой метки
        self.label_metrics = tk.Label(self.metrics_window, text="Здесь могут быть ваши метрики и графики")
        self.label_metrics.pack(padx=10, pady=10)
        self.controller.calculate_metrics()
        # Пример: добавление кнопки для закрытия окна
        close_button = tk.Button(self.metrics_window, text="График", command=self.controller.grafik)
        close_button.pack(padx=10, pady=10)
        # Пример: добавление кнопки для закрытия окна
        close_button = tk.Button(self.metrics_window, text="Закрыть", command=self.metrics_window.destroy)
        close_button.pack(padx=10, pady=10)