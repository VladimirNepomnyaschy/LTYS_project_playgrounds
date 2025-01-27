""" Playground """
import json
import time
import whisper
import utils


def speech_to_text(speech: __file__, language: str):
    model = whisper.load_model("small")
    result = model.transcribe(speech, language=language, fp16=False)
    # with open(r"/home/nepomn-vladimir/IT_learning/Projects/ListenToYourSound/recognition.txt", "w", encoding="utf-8") as output_file:
    #     output_file.write(result["text"])
    return result["text"]


start_time = time.perf_counter()
speech_to_text(
    r"/home/nepomn-vladimir/IT_learning/Projects/ListenToYourSound/1.mp3", 'ru')
end_time = time.perf_counter()
recognition_duration = end_time - start_time
# print(recognition_duration)


# def measure_time(func) -> int:
#     start_time = time.perf_counter()
#     result = func()
#     end_time = time.perf_counter()
#     recognition_duration = round((end_time - start_time) * 1000)
#     return result, recognition_duration

# print(measure_time(lambda: speech_to_text(r"./1.mp3", "ru")))


# Список языков можно взять из питона: whisper.tokenizer.LANGUAGES.keys()
# print(whisper.tokenizer.LANGUAGES)

option_lang_str = ["<option value="">Auto</option>"]
for lang_short, lang_discription in whisper.tokenizer.LANGUAGES.items():
    option_lang_str.append(
        f"<option value={lang_short}>{lang_discription}</option>")
# print(''.join(option_lang_str))


available_languages = {"Auto": ""}
for key, value in whisper.tokenizer.LANGUAGES.items():
    available_languages[value.capitalize()] = available_languages.get(
        value, key)
    langs_dict = json.dumps(available_languages, indent=3)
# print(json.dumps(available_languages, indent=3))

# Проверка подключаемости модуля utils
# print(utils.measure_time(lambda: speech_to_text(r"./1.mp3", "ru")))
