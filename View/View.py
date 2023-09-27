import tkinter as tk

from Controller import Controller
class View:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("Пример MVC с Tkinter")

        # Создаем кнопку для загрузки файла и размещаем ее внизу
        self.button = tk.Button(root, text="Загрузить Word файл", command=self.controller.open_word_file)
        self.button.grid(row=1, column=1, pady=10)  # Размещаем кнопку внизу

        # Создаем текстовое поле для отображения информации о загруженных файлах
        self.log_text = tk.Text(root, height=10, width=60)
        self.log_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.log_text.config(state=tk.DISABLED)
        # Создаем метку для пояснительного текста
        self.query_label = tk.Label(root, text="Введите языковой запрос:", padx=10, pady=5)
        self.query_label.grid(row=2, column=1)

        # Создаем поле для ввода языкового запроса
        self.query_entry = tk.Entry(root, width=40)
        self.query_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

        # Создаем кнопку для выполнения запроса
        self.execute_button = tk.Button(root, text="Выполнить запрос", command=self.controller.start)
        self.execute_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)


        # Задаем конфигурацию сетки для растяжения метки на всю доступную ширину
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def show_open_files_button(self):
        # Создаем кнопку для открытия файлов
        self.listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.listbox.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
        self.controller.update_file_list()
        self.open_files_button = tk.Button(self.root, text="Открыть файл", command=self.controller.open_new_files)
        self.open_files_button.grid(row=4, column=2, columnspan=1, padx=10, pady=10)
        self.show_metrics_button = tk.Button(self.root, text="Показать метрики и график", command=self.show_metrics_results)
        self.show_metrics_button.grid(row=5, column=1, columnspan=2, padx=10, pady=10)



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