import sys
from docx2pdf import convert
import os
import time

#Конвертируем файл
def converting(path):             #! используй *args - для принимания множества аргументов
    now_time = time.localtime()
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S", now_time)
    output = path.split('.')[0] + "_" + now_time + '.pdf'
    try:
        convert(path, output)
    except Exception as e:
        print(f"Ошибка: {e}\nВозможно файл не относится к .docx\nПопробуйте снова.")
        os.system("pause")
        os.system("cls")
        return hand_input()

def love_check(hand_path):
    if hand_path == "love" or hand_path == "Love" or \
        hand_path == "Никита" or hand_path == "никита" or \
        hand_path == "Никитка" or hand_path == "никитка":
            os.system("cls")
            print("                                                     Я никитка")
            print("\n\n\n\n\n\n\n\n                   И я люблю ")
            print("\n\n\n\n\n\n\n\n                                                                                           Залиньку🥰")
            os.system("pause >nul")
            os.system("cls")
            hand_input()
    else:
        return hand_path


#Проверяем ввод на ошибки
def safe_input(func):
    def wrapper():
        while True:
            hand_path = input("Введите путь к файлу: ")
            love_check(hand_path)
            hand_path = hand_path.strip("\"'")
            if (hand_path and os.path.isfile(hand_path)):
                print(f"Файл: \"{hand_path}\" Существует")
                return func(hand_path)
            else:
                print("Неверный путь или файл не существует. Пожалуйста, попробуйте снова.")
    return wrapper

# Ручной ввод
@safe_input
def hand_input(hand_path):
    converting(hand_path)

# Главная функция
def main():
    if len(sys.argv) < 2:         # Ручной ввод
        hand_input()
        sys.exit(0)
    else:                         # Автоматический ввод
        converting(sys.argv[1])
        
if __name__ == "__main__":
    main()