import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller() #Работаем через контроллер в случае, если не производится авто клик в браузере на отправку

def send_message_inst():
    phone = ['+79779712579', '+79149090459'] #Вставляем номера телефонов с +
    message = 'привет!'
    try:
        for elem in phone: #Перебираем телефоны
            pywhatkit.sendwhatmsg_instantly(phone_no=elem, message=message, tab_close=True) #Создаем основной объект
            time.sleep(10)
            pyautogui.click() #кликаем на область экрана, чтоб удостовериться, что рабочая область активна
            time.sleep(2)
            keyboard.press(Key.enter) #Имитируем ручной клик на Enter
            keyboard.release(Key.enter)
    except Exception as e:
        print(str(e))

def main():
    send_message_inst()

if __name__ == "__main__":
    main()
