"""TKinter speech recognition app (learning TKinter)"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
import whisper
import os

# Переменной app присваиваем экземпляр класса TK
app = Tk()
# определяем название заголовка окна
app.title("Listen to your sound")
# определяем прозрачность нашего окна и его фон
app.attributes("-alpha", 0.5)
app.config(background="#a8d182")
# определяем иконку на окне
favicon = PhotoImage(file="favicon.png")
app.iconphoto(False, favicon)
# определяем размер окна в пикселях и отступы от левого верхнего края экрана при запуске
app.geometry("1000x800+500+50")
app.resizable(False, False)  # запрет на изменение размеров по ширине и высоте

FILE_PATH = ''


def choose_file():
    "Функция, возвращающая путь к файлу для распознавания"
    try:
        global FILE_PATH
        FILE_PATH = filedialog.askopenfilename()
        file_name_label[
            "text"] = f"Имя файла для распознавания: {os.path.basename(FILE_PATH)}"
    except:
        print("Выберите аудиофайл для распознавания в формате .wav или .mp3!")


def speech_to_text(speech: str = FILE_PATH, language: str = "ru"):
    start_time = time.perf_counter()
    model = whisper.load_model("small")
    result = model.transcribe(FILE_PATH, language=language, fp16=False)
    end_time = time.perf_counter()
    recognition_duration = round((end_time - start_time) * 1000)
    recognition_text_label["text"] = f"""Распознанный текст: {result["text"]}
Длительность расознавания: {recognition_duration} мс"""


# Текстовая метка с выводом распознанного текста
recognition_text_label = ttk.Label(font=("Arial", 14))
recognition_text_label.pack(expand=True)

# Текстовая метка с выводом названия файла
file_name_label = ttk.Label(
    text="Выберите файл!", font=("Arial", 14))
file_name_label.pack(expand=True)

# Кнопка выбора файла
choise_file_btn = Button(text="Выбрать файл",
                         bg='blue',
                         fg="white",
                         font=("arial", 12, "bold"), command=choose_file)
choise_file_btn.place(x=150, y=650)
# choise_file_btn.pack()    # размещаем кнопку в окне

# Кнопка отправки аудиофайла для распознавания
send_file_btn = Button(text="Отправить файл",
                       bg='blue',
                       fg="white",
                       font=("arial", 12, "bold"), command=speech_to_text)
send_file_btn.place(x=700, y=650)
# send_file_btn.pack()    # размещаем кнопку в окне


# start_time = time.perf_counter()
# speech_to_text(
#     r"/home/nepomn-vladimir/IT_learning/Projects/ListenToYourSound/1.mp3", 'ru')
# end_time = time.perf_counter()
# recognition_duration = end_time - start_time
# print(recognition_duration)


app.mainloop()  # Для запуска приложения необходимо добавление главного цикла
